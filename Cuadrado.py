from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget


class Cuadrado(QWidget):
    def __init__(self, color):
        super().__init__()
        paleta = QPalette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setAutoFillBackground(True)
        self.setPalette(paleta)
