import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton, \
    QRadioButton, QCheckBox, QTextEdit, QLineEdit, QComboBox
from Cuadrado import Cuadrado

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()


        # ---- Caja Vertical ----
        caja_vertical = QVBoxLayout()
        self.stack = QStackedLayout()
        caja_vertical.addLayout(self.stack)

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
        self.set_stack_por_nombre("white")


        # ----- Caja Horizontal 1 -----
        caja_horizontal = QHBoxLayout()
        caja_vertical.addLayout(caja_horizontal)

        ## Creación botones
        boton_azul = QPushButton("Azul")
        boton_rojo = QPushButton("Rojo")
        boton_verde = QPushButton("Verde")
        boton_naranja = QPushButton("Naranja")

        ## OnClick botones
        boton_azul.pressed.connect(self.on_boton_azul)
        boton_rojo.pressed.connect(self.on_boton_rojo)
        boton_verde.pressed.connect(self.on_boton_verde)
        boton_naranja.pressed.connect(self.on_boton_naranja)

        ## Add botones
        caja_horizontal.addWidget(boton_azul)
        caja_horizontal.addWidget(boton_rojo)
        caja_horizontal.addWidget(boton_verde)
        caja_horizontal.addWidget(boton_naranja)


        # ----- Caja Horizontal 2 -----
        caja_horizontal2 = QHBoxLayout()
        caja_vertical.addLayout(caja_horizontal2)

        ## Creación botones
        self.boton_rojo_radio = QRadioButton("Rojo")
        self.boton_azul_radio = QRadioButton("Azul")
        self.boton_verde_radio = QRadioButton("Verde")
        self.boton_naranja_radio = QRadioButton("Naranja")

        ## OnClick botones
        self.boton_azul_radio.pressed.connect(self.on_boton_azul)
        self.boton_rojo_radio.pressed.connect(self.on_boton_rojo)
        self.boton_verde_radio.pressed.connect(self.on_boton_verde)
        self.boton_naranja_radio.pressed.connect(self.on_boton_naranja)

        ## Add botones
        caja_horizontal2.addWidget(self.boton_azul_radio)
        caja_horizontal2.addWidget(self.boton_rojo_radio)
        caja_horizontal2.addWidget(self.boton_verde_radio)
        caja_horizontal2.addWidget(self.boton_naranja_radio)


        # ----- Caja Horizontal 3 -----
        caja_horizontal3 = QHBoxLayout()
        caja_vertical.addLayout(caja_horizontal3)

        ## Creación botones
        self.boton_rojo_check = QCheckBox("Rojo")
        self.boton_azul_check = QCheckBox("Azul")
        self.boton_verde_check = QCheckBox("Verde")
        self.boton_naranja_check = QCheckBox("Naranja")

        ## Add botones
        caja_horizontal3.addWidget(self.boton_azul_check)
        caja_horizontal3.addWidget(self.boton_rojo_check)
        caja_horizontal3.addWidget(self.boton_verde_check)
        caja_horizontal3.addWidget(self.boton_naranja_check)

        # ----- Caja Horizontal 4 -----
        caja_horizontal4 = QHBoxLayout()
        caja_vertical.addLayout(caja_horizontal4)

        ## Creacion combo box
        combo_box = QComboBox()
        combo_box.addItems(["Rojo", "Azul", "Verde", "Naranja"])

        ## Add combo box
        caja_horizontal4.addWidget(combo_box)

        # ----- Settings -----
        contenedor = QWidget()
        contenedor.setLayout(caja_vertical)
        self.setCentralWidget(contenedor)

        self.setWindowTitle("Ejemplo Stacked Layout")
        self.setMinimumSize(400, 180)
        self.show()

    def on_boton_rojo(self):
        # self.stack.setCurrentIndex(0)  # Cambiar al widget rojo
        self.set_stack_por_nombre("red")
        self.check_toggle()
        self.boton_rojo_radio.toggle()
        self.boton_rojo_check.click()

    def on_boton_azul(self):
        self.set_stack_por_nombre("blue")
        self.check_toggle()
        self.boton_azul_radio.toggle()
        self.boton_azul_check.click()

    def on_boton_verde(self):
        self.set_stack_por_nombre("green")
        self.check_toggle()
        self.boton_verde_radio.toggle()
        self.boton_verde_check.click()

    def on_boton_naranja(self):
        self.set_stack_por_nombre("orange")
        self.check_toggle()
        self.boton_naranja_radio.toggle()
        self.boton_naranja_check.toggle()

    def check_toggle(self):
        if self.boton_rojo_check.isChecked(): self.boton_rojo_check.toggle()
        if self.boton_azul_check.isChecked(): self.boton_azul_check.toggle()
        if self.boton_verde_check.isChecked(): self.boton_verde_check.toggle()
        if self.boton_naranja_check.isChecked(): self.boton_naranja_check.toggle()

    def set_stack_por_nombre(self, nombre):
        widget = self.diccionario_widgets.get(nombre)
        if widget:
            self.stack.setCurrentWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear la aplicación
    window = VentanaPrincipal()  # Crear la ventana principal
    app.exec()