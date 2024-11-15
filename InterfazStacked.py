import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton, \
    QRadioButton, QCheckBox
from Cuadrado import Cuadrado

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()


        # ---- Caja Vertical ----
        cajaVertical = QVBoxLayout()
        self.stack = QStackedLayout()
        cajaVertical.addLayout(self.stack)

        ## Creación widgets
        self.diccionario_widgets = {
            "red": Cuadrado("red"),
            "blue": Cuadrado("blue"),
            "green": Cuadrado("green"),
            "orange": Cuadrado("orange"),
            "purple": Cuadrado("purple"),
            "black": Cuadrado("black"),
            "white": Cuadrado("white"),
        }

        ## Add widgets
        for widget in self.diccionario_widgets.values():
            self.stack.addWidget(widget)

        ## Widget al inciiar
        self.setStackPorNombre("white")


        # ----- Caja Horizontal 1 -----
        cajaHorizontal = QHBoxLayout()
        cajaVertical.addLayout(cajaHorizontal)

        ## Creación botones
        botonAzul = QPushButton("Azul")
        botonRojo = QPushButton("Rojo")
        botonVerde = QPushButton("Verde")
        botonNaranja = QPushButton("Naranja")

        ## OnClick botones
        botonAzul.pressed.connect(self.on_Boton_Azul)
        botonRojo.pressed.connect(self.on_Boton_Rojo)
        botonVerde.pressed.connect(self.on_Boton_Verde)
        botonNaranja.pressed.connect(self.on_Boton_Naranja)

        ## Add botones
        cajaHorizontal.addWidget(botonAzul)
        cajaHorizontal.addWidget(botonRojo)
        cajaHorizontal.addWidget(botonVerde)
        cajaHorizontal.addWidget(botonNaranja)


        # ----- Caja Horizontal 2 -----
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


        # ----- Caja Horizontal 3 -----
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

        # ----- Settings -----
        contenedor = QWidget()
        contenedor.setLayout(cajaVertical)
        self.setCentralWidget(contenedor)

        self.setWindowTitle("Ejemplo Stacked Layout")
        self.setMinimumSize(400, 150)
        self.show()

    def on_Boton_Rojo(self):
        # self.stack.setCurrentIndex(0)  # Cambiar al widget rojo
        self.setStackPorNombre("red")
        self.botonRojoRadio.toggle()
        self.checkToggle()
        self.botonRojoCheck.click()

    def on_Boton_Azul(self):
        self.setStackPorNombre("blue")
        self.botonAzulRadio.toggle()
        self.checkToggle()
        self.botonAzulCheck.click()

    def on_Boton_Verde(self):
        self.setStackPorNombre("green")
        self.botonVerdeRadio.toggle()
        self.checkToggle()
        self.botonVerdeCheck.click()

    def on_Boton_Naranja(self):
        self.setStackPorNombre("orange")
        self.botonNaranjaRadio.toggle()
        self.checkToggle()
        self.botonNaranjaCheck.toggle()

    def checkToggle(self):
        if self.botonRojoCheck.isChecked(): self.botonRojoCheck.toggle()
        if self.botonAzulCheck.isChecked(): self.botonAzulCheck.toggle()
        if self.botonVerdeCheck.isChecked(): self.botonVerdeCheck.toggle()
        if self.botonNaranjaCheck.isChecked(): self.botonNaranjaCheck.toggle()

    def setStackPorNombre(self, nombre):
        widget = self.diccionario_widgets.get(nombre)
        if widget:
            self.stack.setCurrentWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear la aplicación
    window = VentanaPrincipal()  # Crear la ventana principal
    app.exec()