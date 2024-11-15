import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton, \
    QRadioButton
from Cuadrado import Cuadrado

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Stacked Layout")  # Establecer el título de la ventana
        self.setMinimumSize(400, 400)  # Establecer el tamaño mínimo de la ventana

        cajaVertical = QVBoxLayout()  # Crear un layout vertical

        self.stack = QStackedLayout()  # Crear un layout apilado
        self.stack.addWidget(Cuadrado("red"))  # Añadir un widget rojo
        self.stack.addWidget(Cuadrado("blue"))  # Añadir un widget azul
        self.stack.addWidget(Cuadrado("green"))  # Añadir un widget verde
        self.stack.addWidget(Cuadrado("orange"))  # Añadir un widget naranja
        self.stack.setCurrentIndex(0)  # Establecer el widget rojo como el predeterminado

        cajaVertical.addLayout(self.stack)  # Añadir el layout apilado al layout vertical

        cajaHorizontal = QHBoxLayout()  # Crear un layout horizontal
        cajaVertical.addLayout(cajaHorizontal)  # Añadir el layout horizontal al layout vertical

        # Botón Rojo
        botonRojo = QPushButton("Rojo")  # Crear un botón con el texto "Rojo"
        cajaHorizontal.addWidget(botonRojo)  # Añadir el botón al layout horizontal
        botonRojo.pressed.connect(self.on_Boton_Rojo)  # Conectar la señal pressed del botón a la función on_Boton_Rojo

        # Botón Azul
        botonAzul = QPushButton("Azul")
        cajaHorizontal.addWidget(botonAzul)
        botonAzul.pressed.connect(self.on_Boton_Azul)

        # Botón Verde
        botonVerde = QPushButton("Verde")
        cajaHorizontal.addWidget(botonVerde)
        botonVerde.pressed.connect(self.on_Boton_Verde)

        # Botón Naranja
        botonNaranja = QPushButton("Naranja")
        cajaHorizontal.addWidget(botonNaranja)
        botonNaranja.pressed.connect(self.on_Boton_Naranja)

        cajaHorizontal2 = QHBoxLayout()

        botonRojoRadio = QRadioButton("Rojo")
        cajaHorizontal2.addWidget(botonRojoRadio)

        botonVerdeRadio = QRadioButton("Verde")
        cajaHorizontal2.addWidget(botonVerdeRadio)

        botonVerdeRadio.click()

        cajaVertical.addLayout(cajaHorizontal2)

        contenedor = QWidget()  # Crear un widget contenedor
        contenedor.setLayout(cajaVertical)  # Establecer el layout vertical como el layout del contenedor
        self.setCentralWidget(contenedor)  # Establecer el contenedor como el widget central de la ventana
        self.show()  # Mostrar la ventana

    def on_Boton_Rojo(self):
        self.stack.setCurrentIndex(0)  # Cambiar al widget rojo

    def on_Boton_Azul(self):
        self.stack.setCurrentIndex(1)  # Cambiar al widget azul

    def on_Boton_Verde(self):
        self.stack.setCurrentIndex(2)  # Cambiar al widget verde

    def on_Boton_Naranja(self):
        self.stack.setCurrentIndex(3)  # Cambiar al widget naranja

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear la aplicación
    window = VentanaPrincipal()  # Crear la ventana principal
    app.exec()