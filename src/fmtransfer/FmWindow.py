# Form implementation generated from reading ui file 'fm-transfer.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FmTransfer(object):
    def setupUi(self, FmTransfer):
        FmTransfer.setObjectName("FmTransfer")
        FmTransfer.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        FmTransfer.resize(573, 731)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FmTransfer.sizePolicy().hasHeightForWidth())
        FmTransfer.setSizePolicy(sizePolicy)
        FmTransfer.setMinimumSize(QtCore.QSize(530, 630))
        FmTransfer.setMaximumSize(QtCore.QSize(800, 800))
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::MediaSeekForward")
        FmTransfer.setWindowIcon(icon)
        FmTransfer.setAutoFillBackground(False)
        FmTransfer.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=FmTransfer)
        self.centralwidget.setObjectName("centralwidget")
        self.centralGridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.centralGridLayout.setObjectName("centralGridLayout")
        self.qhBoxHorizontalLayout = QtWidgets.QHBoxLayout()
        self.qhBoxHorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.qhBoxHorizontalLayout.setObjectName("qhBoxHorizontalLayout")
        self.pttGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pttGroupBox.sizePolicy().hasHeightForWidth())
        self.pttGroupBox.setSizePolicy(sizePolicy)
        self.pttGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.pttGroupBox.setMaximumSize(QtCore.QSize(130, 100))
        self.pttGroupBox.setObjectName("pttGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pttGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pttReleasedRadioButton = QtWidgets.QRadioButton(parent=self.pttGroupBox)
        self.pttReleasedRadioButton.setChecked(True)
        self.pttReleasedRadioButton.setAutoExclusive(True)
        self.pttReleasedRadioButton.setObjectName("pttReleasedRadioButton")
        self.verticalLayout_3.addWidget(self.pttReleasedRadioButton)
        self.pttPressedRadioButton = QtWidgets.QRadioButton(parent=self.pttGroupBox)
        self.pttPressedRadioButton.setAutoExclusive(True)
        self.pttPressedRadioButton.setObjectName("pttPressedRadioButton")
        self.verticalLayout_3.addWidget(self.pttPressedRadioButton)
        self.signalLogic = QtWidgets.QCheckBox(parent=self.pttGroupBox)
        self.signalLogic.setObjectName("signalLogic")
        self.verticalLayout_3.addWidget(self.signalLogic)
        self.qhBoxHorizontalLayout.addWidget(self.pttGroupBox)
        self.toolGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.toolGroupBox.setMaximumSize(QtCore.QSize(130, 100))
        self.toolGroupBox.setObjectName("toolGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.toolGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ggRadioButton = QtWidgets.QRadioButton(parent=self.toolGroupBox)
        self.ggRadioButton.setChecked(True)
        self.ggRadioButton.setObjectName("ggRadioButton")
        self.verticalLayout_5.addWidget(self.ggRadioButton)
        self.quietRadioButton = QtWidgets.QRadioButton(parent=self.toolGroupBox)
        self.quietRadioButton.setObjectName("quietRadioButton")
        self.verticalLayout_5.addWidget(self.quietRadioButton)
        self.qhBoxHorizontalLayout.addWidget(self.toolGroupBox)
        self.protocolGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.protocolGroupBox.setMaximumSize(QtCore.QSize(180, 100))
        self.protocolGroupBox.setObjectName("protocolGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.protocolGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ggProtocolComboBox = QtWidgets.QComboBox(parent=self.protocolGroupBox)
        self.ggProtocolComboBox.setObjectName("ggProtocolComboBox")
        self.ggProtocolComboBox.addItem("")
        self.ggProtocolComboBox.addItem("")
        self.ggProtocolComboBox.addItem("")
        self.ggProtocolComboBox.addItem("")
        self.ggProtocolComboBox.addItem("")
        self.ggProtocolComboBox.addItem("")
        self.ggProtocolComboBox.addItem("")
        self.ggProtocolComboBox.addItem("")
        self.ggProtocolComboBox.addItem("")
        self.verticalLayout.addWidget(self.ggProtocolComboBox)
        self.quietProtocolComboBox = QtWidgets.QComboBox(parent=self.protocolGroupBox)
        self.quietProtocolComboBox.setObjectName("quietProtocolComboBox")
        self.quietProtocolComboBox.addItem("")
        self.quietProtocolComboBox.addItem("")
        self.quietProtocolComboBox.addItem("")
        self.quietProtocolComboBox.addItem("")
        self.quietProtocolComboBox.addItem("")
        self.quietProtocolComboBox.addItem("")
        self.quietProtocolComboBox.addItem("")
        self.verticalLayout.addWidget(self.quietProtocolComboBox)
        self.qhBoxHorizontalLayout.addWidget(self.protocolGroupBox)
        self.signalGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signalGroupBox.sizePolicy().hasHeightForWidth())
        self.signalGroupBox.setSizePolicy(sizePolicy)
        self.signalGroupBox.setMinimumSize(QtCore.QSize(130, 0))
        self.signalGroupBox.setMaximumSize(QtCore.QSize(130, 100))
        self.signalGroupBox.setObjectName("signalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.signalGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dsrRadioButton = QtWidgets.QRadioButton(parent=self.signalGroupBox)
        self.dsrRadioButton.setChecked(True)
        self.dsrRadioButton.setAutoExclusive(True)
        self.dsrRadioButton.setObjectName("dsrRadioButton")
        self.verticalLayout_2.addWidget(self.dsrRadioButton)
        self.rtsRadioButton = QtWidgets.QRadioButton(parent=self.signalGroupBox)
        self.rtsRadioButton.setAutoExclusive(True)
        self.rtsRadioButton.setObjectName("rtsRadioButton")
        self.verticalLayout_2.addWidget(self.rtsRadioButton)
        self.qhBoxHorizontalLayout.addWidget(self.signalGroupBox)
        self.centralGridLayout.addLayout(self.qhBoxHorizontalLayout, 0, 0, 1, 1)
        self.messages = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messages.sizePolicy().hasHeightForWidth())
        self.messages.setSizePolicy(sizePolicy)
        self.messages.setAcceptDrops(False)
        self.messages.setUndoRedoEnabled(False)
        self.messages.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.NoWrap)
        self.messages.setReadOnly(True)
        self.messages.setCenterOnScroll(False)
        self.messages.setObjectName("messages")
        self.centralGridLayout.addWidget(self.messages, 1, 0, 1, 1)
        self.signalLedHorizontalLayout = QtWidgets.QHBoxLayout()
        self.signalLedHorizontalLayout.setObjectName("signalLedHorizontalLayout")
        self.checkSignalButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkSignalButton.sizePolicy().hasHeightForWidth())
        self.checkSignalButton.setSizePolicy(sizePolicy)
        self.checkSignalButton.setMinimumSize(QtCore.QSize(98, 0))
        self.checkSignalButton.setObjectName("checkSignalButton")
        self.signalLedHorizontalLayout.addWidget(self.checkSignalButton)
        self.led = Led(parent=self.centralwidget)
        self.led.setOn(False)
        self.led.setLightColor(QtGui.QColor(255, 0, 0))
        self.led.setObjectName("led")
        self.signalLedHorizontalLayout.addWidget(self.led)
        self.serialComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialComboBox.sizePolicy().hasHeightForWidth())
        self.serialComboBox.setSizePolicy(sizePolicy)
        self.serialComboBox.setObjectName("serialComboBox")
        self.signalLedHorizontalLayout.addWidget(self.serialComboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.signalLedHorizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.signalLedHorizontalLayout.addWidget(self.pushButton)
        self.centralGridLayout.addLayout(self.signalLedHorizontalLayout, 2, 0, 1, 1)
        self.sendFilehorizontalLayout = QtWidgets.QHBoxLayout()
        self.sendFilehorizontalLayout.setObjectName("sendFilehorizontalLayout")
        self.chooseSendFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.chooseSendFileButton.setMinimumSize(QtCore.QSize(98, 0))
        self.chooseSendFileButton.setObjectName("chooseSendFileButton")
        self.sendFilehorizontalLayout.addWidget(self.chooseSendFileButton)
        self.sendFileLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.sendFileLineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sendFileLineEdit.setAcceptDrops(False)
        self.sendFileLineEdit.setReadOnly(True)
        self.sendFileLineEdit.setObjectName("sendFileLineEdit")
        self.sendFilehorizontalLayout.addWidget(self.sendFileLineEdit)
        self.sendFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sendFileButton.setMinimumSize(QtCore.QSize(80, 0))
        self.sendFileButton.setObjectName("sendFileButton")
        self.sendFilehorizontalLayout.addWidget(self.sendFileButton)
        self.centralGridLayout.addLayout(self.sendFilehorizontalLayout, 3, 0, 1, 1)
        self.receiveHorizontalLayout = QtWidgets.QHBoxLayout()
        self.receiveHorizontalLayout.setObjectName("receiveHorizontalLayout")
        self.chooseRecvFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.chooseRecvFileButton.setMinimumSize(QtCore.QSize(98, 0))
        self.chooseRecvFileButton.setObjectName("chooseRecvFileButton")
        self.receiveHorizontalLayout.addWidget(self.chooseRecvFileButton)
        self.receiveFileLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.receiveFileLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.receiveFileLineEdit.setAcceptDrops(False)
        self.receiveFileLineEdit.setReadOnly(True)
        self.receiveFileLineEdit.setObjectName("receiveFileLineEdit")
        self.receiveHorizontalLayout.addWidget(self.receiveFileLineEdit)
        self.receiveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.receiveButton.setMinimumSize(QtCore.QSize(80, 0))
        self.receiveButton.setObjectName("receiveButton")
        self.receiveHorizontalLayout.addWidget(self.receiveButton)
        self.centralGridLayout.addLayout(self.receiveHorizontalLayout, 4, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setObjectName("progressBar")
        self.centralGridLayout.addWidget(self.progressBar, 5, 0, 1, 1)
        self.msgHorizontalLayout = QtWidgets.QHBoxLayout()
        self.msgHorizontalLayout.setObjectName("msgHorizontalLayout")
        self.recvMsgButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.recvMsgButton.setObjectName("recvMsgButton")
        self.msgHorizontalLayout.addWidget(self.recvMsgButton)
        self.shortMsg = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.shortMsg.setAcceptDrops(False)
        self.shortMsg.setMaxLength(140)
        self.shortMsg.setObjectName("shortMsg")
        self.msgHorizontalLayout.addWidget(self.shortMsg)
        self.sendMsgButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sendMsgButton.setObjectName("sendMsgButton")
        self.msgHorizontalLayout.addWidget(self.sendMsgButton)
        self.centralGridLayout.addLayout(self.msgHorizontalLayout, 6, 0, 1, 1)
        FmTransfer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=FmTransfer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        FmTransfer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=FmTransfer)
        self.statusbar.setObjectName("statusbar")
        FmTransfer.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(FmTransfer)
        self.ggProtocolComboBox.setCurrentIndex(2)
        self.checkSignalButton.clicked.connect(FmTransfer.check_signal) # type: ignore
        self.dsrRadioButton.toggled['bool'].connect(FmTransfer.toggle_signal) # type: ignore
        self.sendMsgButton.clicked.connect(FmTransfer.send_text) # type: ignore
        self.receiveButton.clicked.connect(FmTransfer.receive_file) # type: ignore
        self.sendFileButton.clicked.connect(FmTransfer.send_file) # type: ignore
        self.chooseSendFileButton.clicked.connect(FmTransfer.choose_send_file) # type: ignore
        self.ggProtocolComboBox.currentIndexChanged['int'].connect(FmTransfer.set_gg_protocol) # type: ignore
        self.chooseRecvFileButton.clicked.connect(FmTransfer.choose_recv_file) # type: ignore
        self.recvMsgButton.clicked.connect(FmTransfer.receive_text) # type: ignore
        self.pttReleasedRadioButton.toggled['bool'].connect(FmTransfer.toggle_ptt) # type: ignore
        self.ggRadioButton.toggled['bool'].connect(FmTransfer.set_tool) # type: ignore
        self.quietProtocolComboBox.currentIndexChanged['int'].connect(FmTransfer.set_quiet_protocol) # type: ignore
        self.pushButton.clicked.connect(FmTransfer.recheck_serial_ports) # type: ignore
        self.signalLogic.clicked['bool'].connect(FmTransfer.set_signal_logic) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FmTransfer)
        FmTransfer.setTabOrder(self.pttReleasedRadioButton, self.pttPressedRadioButton)
        FmTransfer.setTabOrder(self.pttPressedRadioButton, self.ggRadioButton)
        FmTransfer.setTabOrder(self.ggRadioButton, self.quietRadioButton)
        FmTransfer.setTabOrder(self.quietRadioButton, self.ggProtocolComboBox)
        FmTransfer.setTabOrder(self.ggProtocolComboBox, self.quietProtocolComboBox)
        FmTransfer.setTabOrder(self.quietProtocolComboBox, self.dsrRadioButton)
        FmTransfer.setTabOrder(self.dsrRadioButton, self.rtsRadioButton)
        FmTransfer.setTabOrder(self.rtsRadioButton, self.messages)
        FmTransfer.setTabOrder(self.messages, self.checkSignalButton)
        FmTransfer.setTabOrder(self.checkSignalButton, self.serialComboBox)
        FmTransfer.setTabOrder(self.serialComboBox, self.chooseSendFileButton)
        FmTransfer.setTabOrder(self.chooseSendFileButton, self.sendFileLineEdit)
        FmTransfer.setTabOrder(self.sendFileLineEdit, self.sendFileButton)
        FmTransfer.setTabOrder(self.sendFileButton, self.chooseRecvFileButton)
        FmTransfer.setTabOrder(self.chooseRecvFileButton, self.receiveFileLineEdit)
        FmTransfer.setTabOrder(self.receiveFileLineEdit, self.receiveButton)
        FmTransfer.setTabOrder(self.receiveButton, self.recvMsgButton)
        FmTransfer.setTabOrder(self.recvMsgButton, self.shortMsg)
        FmTransfer.setTabOrder(self.shortMsg, self.sendMsgButton)

    def retranslateUi(self, FmTransfer):
        _translate = QtCore.QCoreApplication.translate
        FmTransfer.setWindowTitle(_translate("FmTransfer", "FM-Transfer"))
        self.pttGroupBox.setTitle(_translate("FmTransfer", "PTT"))
        self.pttReleasedRadioButton.setText(_translate("FmTransfer", "Unpressed"))
        self.pttPressedRadioButton.setText(_translate("FmTransfer", "Pressed"))
        self.signalLogic.setText(_translate("FmTransfer", "Reverse logic"))
        self.toolGroupBox.setTitle(_translate("FmTransfer", "Tool"))
        self.ggRadioButton.setText(_translate("FmTransfer", "gg-transfer"))
        self.quietRadioButton.setText(_translate("FmTransfer", "quiet-lib"))
        self.protocolGroupBox.setTitle(_translate("FmTransfer", "Send protocol"))
        self.ggProtocolComboBox.setItemText(0, _translate("FmTransfer", "Normal"))
        self.ggProtocolComboBox.setItemText(1, _translate("FmTransfer", "Fast"))
        self.ggProtocolComboBox.setItemText(2, _translate("FmTransfer", "Fastest"))
        self.ggProtocolComboBox.setItemText(3, _translate("FmTransfer", "[U] Normal"))
        self.ggProtocolComboBox.setItemText(4, _translate("FmTransfer", "[U] Fast"))
        self.ggProtocolComboBox.setItemText(5, _translate("FmTransfer", "[U] Fastest"))
        self.ggProtocolComboBox.setItemText(6, _translate("FmTransfer", "[DT] Normal"))
        self.ggProtocolComboBox.setItemText(7, _translate("FmTransfer", "[DT] Fast"))
        self.ggProtocolComboBox.setItemText(8, _translate("FmTransfer", "[DT] Fastest"))
        self.quietProtocolComboBox.setItemText(0, _translate("FmTransfer", "audible"))
        self.quietProtocolComboBox.setItemText(1, _translate("FmTransfer", "audible-7k-channel-0"))
        self.quietProtocolComboBox.setItemText(2, _translate("FmTransfer", "audible-7k-channel-1"))
        self.quietProtocolComboBox.setItemText(3, _translate("FmTransfer", "cable-64k"))
        self.quietProtocolComboBox.setItemText(4, _translate("FmTransfer", "ultrasonic"))
        self.quietProtocolComboBox.setItemText(5, _translate("FmTransfer", "ultrasonic-3600"))
        self.quietProtocolComboBox.setItemText(6, _translate("FmTransfer", "ultrasonic-whisper"))
        self.signalGroupBox.setTitle(_translate("FmTransfer", "Signal"))
        self.dsrRadioButton.setText(_translate("FmTransfer", "DTR"))
        self.rtsRadioButton.setText(_translate("FmTransfer", "RTS"))
        self.checkSignalButton.setText(_translate("FmTransfer", "Check signal"))
        self.pushButton.setText(_translate("FmTransfer", "Recheck Serial Ports"))
        self.chooseSendFileButton.setText(_translate("FmTransfer", "Choose send file"))
        self.sendFileButton.setText(_translate("FmTransfer", "Send file"))
        self.chooseRecvFileButton.setText(_translate("FmTransfer", "Choose recv file"))
        self.receiveButton.setText(_translate("FmTransfer", "Receive file"))
        self.recvMsgButton.setText(_translate("FmTransfer", "Receive"))
        self.shortMsg.setPlaceholderText(_translate("FmTransfer", "Short message"))
        self.sendMsgButton.setText(_translate("FmTransfer", "Send"))
        self.menuFile.setTitle(_translate("FmTransfer", "File"))
from led import Led
