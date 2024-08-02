from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QWidget
from PyQt6.QtGui import QColor, QPainter, QPen, QRadialGradient, QMouseEvent
from PyQt6.QtCore import Qt, QPointF, pyqtSlot


# noinspection PyPep8Naming
class Led(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(24, 24)
        self.on = True
        self.light_color = QColor.fromRgbF(255, 0, 0)
        self.glow_effect = QGraphicsDropShadowEffect()
        self.glow_effect.setBlurRadius(48)
        self.glow_effect.setColor(self.light_color.lighter(150))
        self.glow_effect.setOffset(0, 0)
        self.glow_effect.setEnabled(False)
        self.setGraphicsEffect(self.glow_effect)

    def isOn(self):
        return self.on

    @pyqtSlot(bool)
    def setOn(self, on):
        self.on = on
        self.glow_effect.setEnabled(self.on)
        self.update()

    def getLightColor(self):
        return self.light_color

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        e.accept()
        if self.parent().parent().pttPressedRadioButton.isChecked():
            self.parent().parent().pttReleasedRadioButton.setChecked(True)
        else:
            self.parent().parent().pttPressedRadioButton.setChecked(True)

    @pyqtSlot(QColor)
    def setLightColor(self, color: QColor):
        self.light_color = color
        self.glow_effect.setColor(self.light_color.lighter(150))
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)

        led_color = self.light_color if self.on else QColor(Qt.GlobalColor.darkGray)

        # definizione di un gradiente radiale per renderizzare il
        # colore del led e simulare una riflessione ambientale chiara sulla sua superficie
        radius = self.width() / 2.0
        radial_gradient = QRadialGradient(QPointF(radius, radius), radius - 1, QPointF(radius, radius / 2.0))
        radial_gradient.setColorAt(0, led_color.lighter(300))
        radial_gradient.setColorAt(0.5, led_color)
        radial_gradient.setColorAt(1, led_color.darker(200))

        # imposta Pen per il contorno e Brush per il filling
        painter.setPen(QPen(Qt.GlobalColor.gray, 2))
        painter.setBrush(radial_gradient)

        # disegna con un'unica direttiva il contorno grigio
        # e riempie l'areaola circolare del led con il gradiente
        painter.drawEllipse(QPointF(radius, radius), radius - 1, radius - 1)

