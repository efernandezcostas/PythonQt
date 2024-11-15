import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget
from PyQt6.QtCore import QTimer
from Cuadrado import Cuadrado

class InterfazPrueba(QMainWindow):
    def __init__(self):
        super().__init__()

        layout_principal = QGridLayout()
        layout_principal.addWidget(Cuadrado("blue"), 0, 0, 1, 2)
        layout_principal.addWidget(Cuadrado("green"), 1, 0)
        layout_principal.addWidget(Cuadrado("green"), 1, 1)
        layout_principal.addWidget(Cuadrado("green"), 2, 0)
        layout_principal.addWidget(Cuadrado("blue"), 2, 1)
        layout_principal.addWidget(Cuadrado("green"), 3, 0)

        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        self.setGeometry(0, 0, 100, 100)
        self.show()

        QTimer.singleShot(0, self.move_window)

    def move_window(self):
        self.move(0, 0)
        self.raise_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    interfaz = InterfazPrueba()
    sys.exit(app.exec())