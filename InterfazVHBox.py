import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel


class InterfazVHBox(QMainWindow):
    def __init__(self):
        super().__init__()

        contenedor = QWidget()
        self.setCentralWidget(contenedor)

        layout_principal = QHBoxLayout()

        layout_principal.setContentsMargins(0,0,0,0)
        # layout_principal.setSpacing(0)

        layout_1 = crear_layout("blue", "red", "green")
        layout_2 = crear_layout("purple")
        layout_3 = crear_layout("orange", "yellow")

        layout_principal.addLayout(layout_1)
        layout_principal.addLayout(layout_2)
        layout_principal.addLayout(layout_3)

        contenedor.setLayout(layout_principal)

        self.setWindowTitle("Cuadrados")
        # self.setMinimumSize(600,400)
        self.show()

def crear_layout(*colores: str):
    layout = QVBoxLayout()
    for i in range(len(colores)):
        layout.addWidget(crear_cuadrado(colores[i]))
    return layout

def crear_cuadrado(color):
    cuadrado = QLabel()
    # cuadrado.setStyleSheet(f"background-color: {color};")             # Forma de poner colores

    paleta = QPalette()                                                 # Otra forma de poner colores
    paleta.setColor(QPalette.ColorRole.Window, QColor(color))
    cuadrado.setAutoFillBackground(True)
    cuadrado.setPalette(paleta)

    return cuadrado

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = InterfazVHBox()
    sys.exit(app.exec())
