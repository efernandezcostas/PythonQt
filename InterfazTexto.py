import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLineEdit, QTextEdit, QPushButton, \
    QVBoxLayout, QSizePolicy


class InterfazTexto(QMainWindow):
    def __init__(self):
        super().__init__()

        contenedor = QWidget()
        self.setCentralWidget(contenedor)

        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        layout_texto = QGridLayout()

        cuadro_nombre = QLineEdit()
        cuadro_nombre.setPlaceholderText("Nombre")
        layout_texto.addWidget(cuadro_nombre, 0, 0)

        cuadro_apellidos = QLineEdit()
        cuadro_apellidos.setPlaceholderText("Apellidos")
        layout_texto.addWidget(cuadro_apellidos, 0, 1)

        cuadro_dni = QLineEdit()
        cuadro_dni.setPlaceholderText("DNI")
        layout_texto.addWidget(cuadro_dni, 0, 2)

        cuadro_edad = QLineEdit()
        cuadro_edad.setPlaceholderText("Edad")
        layout_texto.addWidget(cuadro_edad, 0, 3)

        layout_texto.setColumnStretch(0, 1)
        layout_texto.setColumnStretch(1, 2)
        layout_texto.setColumnStretch(2, 1)
        layout_texto.setColumnStretch(3, 1)
        # layout_texto.setColumnStretch(4, 1)

        layout_principal.addLayout(layout_texto)

        cuadro_resultado = QTextEdit()
        cuadro_resultado.setPlaceholderText("Resultados")
        # layout_principal.addWidget(cuadro_resultado)

        layout_botones = QGridLayout()
        boton_aceptar = QPushButton("Aceptar")
        layout_botones.addWidget(boton_aceptar, 1, 0, 1, 1)

        boton_cancelar = QPushButton("Cancelar")
        layout_botones.addWidget(boton_cancelar, 1, 1, 1, 1)

        boton_editar = QPushButton("Editar")
        layout_botones.addWidget(boton_editar, 1, 2, 1, 1)

        layout_principal.addLayout(layout_botones)

        contenedor.setLayout(layout_principal)

        self.adjustSize()
        self.setWindowTitle("Título")
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    interfaz = InterfazTexto()
    sys.exit(app.exec())

