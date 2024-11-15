import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout

from Cuadrado import Cuadrado
from InterfazVHBox import InterfazVHBox


class InterfazGridBox(QMainWindow):
    def __init__(self):
        super().__init__()

        contenedor = QWidget()
        self.setCentralWidget(contenedor)

        layout_principal = QGridLayout()

        # layout_principal.setContentsMargins(0,0,0,0)
        # layout_principal.setSpacing(0)

        layout_principal.addWidget(Cuadrado("red"), 0, 0)
        layout_principal.addWidget(Cuadrado("blue"), 0, 1, 1, 2)    # QWidget, row, column, rowSpan, columnSpan
        layout_principal.addWidget(Cuadrado("green"), 1, 0, 2, 1)
        layout_principal.addWidget(Cuadrado("pink"), 1, 1, 1, 2)
        layout_principal.addWidget(Cuadrado("orange"), 2, 1)
        layout_principal.addWidget(Cuadrado("yellow"), 2, 2)
        layout_principal.addWidget(InterfazVHBox(), 3, 0, 3, 3)

        contenedor.setLayout(layout_principal)

        self.setWindowTitle("Cuadrados")
        self.setMinimumSize(400,600)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = InterfazGridBox()
    sys.exit(app.exec())
