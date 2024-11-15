import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton, \
    QRadioButton, QCheckBox
from Cuadrado import Cuadrado

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Stacked Layout")  # Establecer el título de la ventana
        self.setMinimumSize(400, 150)  # Establecer el tamaño mínimo de la ventana

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

        # Botón Azul
        botonAzul = QPushButton("Azul")
        cajaHorizontal.addWidget(botonAzul)
        botonAzul.pressed.connect(self.on_Boton_Azul)

        # Botón Rojo
        botonRojo = QPushButton("Rojo")  # Crear un botón con el texto "Rojo"
        cajaHorizontal.addWidget(botonRojo)  # Añadir el botón al layout horizontal
        botonRojo.pressed.connect(self.on_Boton_Rojo)  # Conectar la señal pressed del botón a la función on_Boton_Rojo

        # Botón Verde
        botonVerde = QPushButton("Verde")
        cajaHorizontal.addWidget(botonVerde)
        botonVerde.pressed.connect(self.on_Boton_Verde)

        # Botón Naranja
        botonNaranja = QPushButton("Naranja")
        cajaHorizontal.addWidget(botonNaranja)
        botonNaranja.pressed.connect(self.on_Boton_Naranja)


        # ---- Caja Horizontal 2 ----
        cajaHorizontal2 = QHBoxLayout()
        cajaVertical.addLayout(cajaHorizontal2)

        ## Creación botones
        self.botonRojoRadio = QRadioButton("Rojo")
        self.botonAzulRadio = QRadioButton("Azul")
        self.botonVerdeRadio = QRadioButton("Verde")
        self.botonNaranjaRadio = QRadioButton("Naranja")

        ## OnClick botones
        self.botonAzulRadio.pressed.connect(self.on_Boton_Azul)
        self.botonRojoRadio.pressed.connect(self.on_Boton_Rojo)
        self.botonVerdeRadio.pressed.connect(self.on_Boton_Verde)
        self.botonNaranjaRadio.pressed.connect(self.on_Boton_Naranja)

        ## Add botones
        cajaHorizontal2.addWidget(self.botonAzulRadio)
        cajaHorizontal2.addWidget(self.botonRojoRadio)
        cajaHorizontal2.addWidget(self.botonVerdeRadio)
        cajaHorizontal2.addWidget(self.botonNaranjaRadio)


        # ---- Caja Horizontal 3 ----
        cajaHorizontal3 = QHBoxLayout()
        cajaVertical.addLayout(cajaHorizontal3)

        ## Creación botones
        self.botonRojoCheck = QCheckBox("Rojo")
        self.botonAzulCheck = QCheckBox("Azul")
        self.botonVerdeCheck = QCheckBox("Verde")
        self.botonNaranjaCheck = QCheckBox("Naranja")

        ## Add botones
        cajaHorizontal3.addWidget(self.botonAzulCheck)
        cajaHorizontal3.addWidget(self.botonRojoCheck)
        cajaHorizontal3.addWidget(self.botonVerdeCheck)
        cajaHorizontal3.addWidget(self.botonNaranjaCheck)


        # ---- Settings ----
        contenedor = QWidget()  # Crear un widget contenedor
        contenedor.setLayout(cajaVertical)  # Establecer el layout vertical como el layout del contenedor
        self.setCentralWidget(contenedor)  # Establecer el contenedor como el widget central de la ventana
        self.show()  # Mostrar la ventana

    def on_Boton_Rojo(self):
        self.stack.setCurrentIndex(0)  # Cambiar al widget rojo
        self.botonRojoRadio.toggle()
        self.checkToggle()
        self.botonRojoCheck.click()

    def on_Boton_Azul(self):
        self.stack.setCurrentIndex(1)  # Cambiar al widget azul
        self.botonAzulRadio.toggle()
        self.checkToggle()
        self.botonAzulCheck.click()

    def on_Boton_Verde(self):
        self.stack.setCurrentIndex(2)  # Cambiar al widget verde
        self.botonVerdeRadio.toggle()
        self.checkToggle()
        self.botonVerdeCheck.click()

    def on_Boton_Naranja(self):
        self.stack.setCurrentIndex(3)  # Cambiar al widget naranja
        self.botonNaranjaRadio.toggle()
        self.checkToggle()
        self.botonNaranjaCheck.toggle()

    def checkToggle(self):
        if self.botonRojoCheck.isChecked(): self.botonRojoCheck.toggle()
        if self.botonAzulCheck.isChecked(): self.botonAzulCheck.toggle()
        if self.botonVerdeCheck.isChecked(): self.botonVerdeCheck.toggle()
        if self.botonNaranjaCheck.isChecked(): self.botonNaranjaCheck.toggle()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear la aplicación
    window = VentanaPrincipal()  # Crear la ventana principal
    app.exec()