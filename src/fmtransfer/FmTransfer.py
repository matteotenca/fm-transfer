import os
import re
import tempfile
from pathlib import Path
from typing import Any, Optional

import serial.serialutil
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtSerialPort import QSerialPortInfo
from PyQt6 import QtCore
from serial import Serial
from .FmWindow import Ui_FmTransfer
from ggtransfer import Receiver


class FmTransfer(QMainWindow, Ui_FmTransfer):

    def __init__(self, **kwargs: Any) -> None:
        super(FmTransfer, self).__init__(**kwargs)
        self.setupUi(FmTransfer=self)
        self._serialdevice: Optional[Serial] = None
        self._serial = ""
        available_ports = QSerialPortInfo.availablePorts()
        self._com_ports = ["none"]
        self.serialComboBox.addItem("Choose a serial port...")
        for port in available_ports:
            # qDebug(f"\n"
            #        f"Port: {i.portName()}\n"
            #        f"Location: {i.systemLocation()}\n"
            #        f"Description: {i.description()}\n"
            #        f"Manufacturer: {i.manufacturer()}\n"
            #        f"Serial number: {i.serialNumber()}\n"
            #        f"Vendor Identifier: {i.vendorIdentifier() if i.hasVendorIdentifier() else ''}\n"
            #        f"Product Identifier: {i.productIdentifier() if i.hasProductIdentifier() else ''}\n"
            #        )
            self._com_ports.append(port.systemLocation())
            self.serialComboBox.addItem(port.systemLocation())
        self.serialComboBox.currentIndexChanged.connect(self.reinit_serial)
        self.pttPressedRadioButton.toggled['bool'].connect(self.led.setOn)
        self.pttGroupBox.setDisabled(True)
        self.signalGroupBox.setDisabled(True)
        self._ptt_state: bool = True
        self._signal = True  # DSR, True = RTS
        self._send_filename = None
        self._receive_filename = None
        self._process_send = QtCore.QProcess(self)
        self._process_send.readyRead.connect(self._send_data_ready)
        self._process_send.started.connect(self._send_data_started)
        self._process_send.finished.connect(self._send_data_end)
        self._process_send_msg = QtCore.QProcess(self)
        self._process_send_msg.readyRead.connect(self._send_msg_data_ready)
        self._process_send_msg.started.connect(self._send_msg_data_started)
        self._process_send_msg.finished.connect(self._send_msg_data_end)
        self._process_receive = QtCore.QProcess(self)
        self._process_receive.readyRead.connect(self._receive_data_ready)
        self._process_receive.started.connect(self._receive_data_started)
        self._process_receive.finished.connect(self._receive_data_end)
        self._receive_in_progress = False
        self._send_in_progress = False
        self.progressBar.setMaximum(1)
        self.progressBar.setValue(0)
        self._pieces = 1
        self._current_piece = 0
        self._protocol = 0
        self._crc32 = None
        self._tempfile: Optional[int] = None

    def _send_msg_data_ready(self):
        new = str(self._process_send_msg.readAll().data(), 'utf-8')
        # new = re.sub(r"\r", "\n", new)
        for line in new.splitlines():
            if line.startswith("Piece "):
                match = re.match(r"Piece (\d+)/(\d+)", line)
                if match is not None:
                    self._current_piece = int(match.group(1))
                    self._pieces = int(match.group(2))
                    self.progressBar.setMaximum(self._pieces)
                    self.progressBar.setValue(self._current_piece)
            elif line.startswith("Speed"):
                self.messages.insertPlainText(line + "\n")
                self.messages.ensureCursorVisible()

    def _send_msg_data_started(self):
        self._pieces = 1
        self._current_piece = 0
        self.progressBar.setMaximum(self._pieces)
        self.progressBar.setValue(self._current_piece)

    def _send_msg_data_end(self):
        os.close(self._tempfile)

    def _send_data_ready(self):
        new = str(self._process_send.readAll().data(), 'utf-8')
        # new = re.sub(r"\r", "\n", new)
        for line in new.splitlines():
            if line.startswith("Pieces: "):
                match = re.match(r"Pieces: (\d+)", line)
                if match is not None:
                    self._pieces = int(match.group(1))
                    self.progressBar.setMaximum(self._pieces)
                    self.messages.insertPlainText(line + "\n")
            elif line.startswith("Piece "):
                match = re.match(r"Piece (\d+)", line)
                if match is not None:
                    self._current_piece = int(match.group(1))
                    self.progressBar.setValue(self._current_piece)
            elif line.startswith("Speed") or line.startswith("Sending") or line.startswith("Time"):
                self.messages.insertPlainText(line + "\n")
        self.messages.ensureCursorVisible()

    def _send_data_started(self):
        self._pieces = 1
        self._current_piece = 0
        self.progressBar.setMaximum(self._pieces)
        self.progressBar.setValue(self._current_piece)
        self.sendFileButton.setText("Stop sending")
        self.receiveButton.setDisabled(True)
        self.chooseRecvFileButton.setDisabled(True)
        self.chooseSendFileButton.setDisabled(True)

    def _send_data_end(self):
        if self.pttGroupBox.isEnabled():
            self.pttReleasedRadioButton.setChecked(True)
        self.receiveButton.setDisabled(False)
        self.sendFileButton.setText("Send file")
        self.chooseRecvFileButton.setDisabled(False)
        self.chooseSendFileButton.setDisabled(False)
        self._send_in_progress = False

    def _receive_data_ready(self):
        new = str(self._process_receive.readAll().data(), 'utf-8')
        # new = re.sub(r"\r", "\n", new)
        for line in new.splitlines():
            if line.startswith("Got header"):
                match = re.match(r".*pieces: (\d+)", line)
                if match is not None:
                    self._pieces = int(match.group(1))
                    self.progressBar.setMaximum(self._pieces)
                    self.messages.insertPlainText(f"Got pieces number: {self._pieces}" + "\n")
                match = re.match(r".*CRC32: (.{8}).*", line)
                if match is not None:
                    self._crc32 = match.group(1)
                    self.messages.insertPlainText(f"Got CRC: {self._crc32}" + "\n")
                self.messages.insertPlainText(line + "\n")
            elif line.startswith("Piece "):
                match = re.match(r"Piece (\d+)", line)
                if match is not None:
                    self._current_piece = int(match.group(1))
                    self.progressBar.setValue(self._current_piece)
            elif line.startswith("Speed") or line.find("ERROR") != -1:
                self.messages.insertPlainText(line + "\n")
        self.messages.ensureCursorVisible()

    def _receive_data_started(self):
        self._pieces = 1
        self._current_piece = 0
        self.progressBar.setMaximum(self._pieces)
        self.progressBar.setValue(self._current_piece)
        self.receiveButton.setText("Stop receiving")
        self.sendFileButton.setDisabled(True)
        self.chooseRecvFileButton.setDisabled(True)
        self.chooseSendFileButton.setDisabled(True)

    def _receive_data_end(self):
        self.receiveButton.setText("Receive file")
        self.sendFileButton.setDisabled(False)
        self.chooseRecvFileButton.setDisabled(False)
        self.chooseSendFileButton.setDisabled(False)
        self._receive_in_progress = False

    def reinit_serial(self, index) -> None:
        # noinspection PyUnresolvedReferences
        if self._serialdevice and self._serialdevice.isOpen():
            self._serialdevice.close()
        if index == 0:
            self._serialdevice = None
            self.pttGroupBox.setDisabled(True)
            self.signalGroupBox.setDisabled(True)
        else:
            self.pttGroupBox.setDisabled(False)
            self.signalGroupBox.setDisabled(False)
            self._init_serial(index)
            self._send_signal()
            self.check_signal()

    # noinspection PyUnresolvedReferences
    def _init_serial(self, index) -> None:
        self._serial = self._com_ports[index]
        if index > 0:
            self._serialdevice = Serial(baudrate=9600)
            self._serialdevice.setDTR(1)
            self._serialdevice.setRTS(1)
            self._serialdevice.setPort(self._serial)
            try:
                self._serialdevice.open()
            except serial.serialutil.SerialException as e:
                self.messages.insertPlainText(str(e) + "\n")
                self.messages.ensureCursorVisible()
                self.serialComboBox.setCurrentIndex(0)
            except Exception as e:
                self.messages.insertPlainText(str(e) + "\n")
                self.messages.ensureCursorVisible()

    # noinspection PyUnresolvedReferences
    def _send_signal(self) -> None:
        if self._serialdevice and self._serialdevice.isOpen():
            if self._ptt_state:
                self._serialdevice.dtr = 1
                self._serialdevice.rts = 1
            else:
                if self._signal:
                    self._serialdevice.dtr = 0
                    self._serialdevice.rts = 1
                else:
                    self._serialdevice.dtr = 1
                    self._serialdevice.rts = 0

    def check_signal(self) -> None:
        # noinspection PyUnresolvedReferences
        if self._serialdevice and self._serialdevice.isOpen():
            if self._signal:
                if self._serialdevice.dtr:
                    self.messages.insertPlainText("Serial 1 DTR signal UP\n")
                else:
                    self.messages.insertPlainText("Serial 1 DTR signal DOWN\n")
            else:
                if self._serialdevice.rts:
                    self.messages.insertPlainText("Serial 1 RTS signal UP\n")
                else:
                    self.messages.insertPlainText("Serial 1 RTS signal DOWN\n")
        self.messages.ensureCursorVisible()

    def toggle_ptt(self, checked: bool) -> None:
        # noinspection PyUnresolvedReferences
        if self._serialdevice and self._serialdevice.isOpen():
            self._ptt_state = checked
            self._send_signal()
            self.check_signal()

    def toggle_signal(self, signal: bool) -> None:
        # noinspection PyUnresolvedReferences
        if self._serialdevice and self._serialdevice.isOpen():
            self._signal = signal
            self._send_signal()
            self.check_signal()

    def send_file(self) -> None:
        if not self._send_in_progress:
            if not self._send_filename or not Path(self._send_filename).is_file():
                self.choose_send_file()
            if Path(self._send_filename).is_file():
                if self.pttGroupBox.isEnabled():
                    self.pttPressedRadioButton.setChecked(True)
                ex = "gg-transfer"
                argss = f"send -p {self._protocol} -f -i".split(" ")
                # noinspection PyTypeChecker
                argss.append(self._send_filename)
                self._process_send.setProcessChannelMode(QtCore.QProcess.ProcessChannelMode.MergedChannels)
                self._process_send.start(ex, argss)
                self._send_in_progress = True
        else:
            if self.pttGroupBox.isEnabled():
                self.pttReleasedRadioButton.setChecked(True)
            self._process_send.kill()
            self._send_in_progress = False

    def receive_file(self) -> None:
        if not self._receive_in_progress:
            if not self._receive_filename:
                self.choose_recv_file()
            if self._receive_filename:
                ex = "gg-transfer"
                argss = "receive -f -w -o".split(" ")
                # noinspection PyTypeChecker
                argss.append(self._receive_filename)
                self._process_receive.setProcessChannelMode(QtCore.QProcess.ProcessChannelMode.MergedChannels)
                self._process_receive.start(ex, argss)
                self._receive_in_progress = True
        else:
            self._process_receive.kill()
            self._receive_in_progress = False

    def send_text(self) -> None:
        msg = self.shortMsg.text()
        if msg:
            self._tempfile, name = tempfile.mkstemp(text=True)
            os.write(self._tempfile, msg.encode("utf-8"))
            ex = "gg-transfer"
            argss = f"send -p {self._protocol} -i {name}".split(" ")
            self._process_send_msg.setProcessChannelMode(QtCore.QProcess.ProcessChannelMode.MergedChannels)
            self._process_send_msg.start(ex, argss)

    def receive_text(self) -> None:
        r = Receiver()
        msg = r.receive()
        if msg:
            self.messages.insertPlainText(msg + "\n")
            self.messages.ensureCursorVisible()

    def set_protocol(self, protocol: int) -> None:
        self._protocol = protocol

    def choose_recv_file(self) -> None:
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self._receive_filename = selected_files[0]
            short_fname = ('...' + self._receive_filename[-20:]) if len(
                self._receive_filename) > 20 else self._receive_filename
            self.receiveFileLineEdit.setText(short_fname)

    def choose_send_file(self) -> None:
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self._send_filename = selected_files[0]
            short_fname = ('...' + self._send_filename[-20:]) if len(
                self._send_filename) > 20 else self._send_filename
            self.sendFileLineEdit.setText(short_fname)
