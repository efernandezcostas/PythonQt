import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QTabWidget, QWidget, QVBoxLayout

from Cuadrado import Cuadrado
from InterfazGridBox import InterfazGridBox
from InterfazVHBox import InterfazVHBox


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        tab_widget = QTabWidget()
        tab_widget.addTab(Cuadrado("red"), "Rojo")
        tab_widget.addTab(Cuadrado("blue"), "Azul")
        tab_widget.addTab(Cuadrado("green"), "Verde")
        tab_widget.addTab(Cuadrado("yellow"), "Amarillo")
        tab_widget.addTab(InterfazVHBox(), "Layout")

        tab_widget_2 = QTabWidget()
        tab_widget_2.addTab(Cuadrado("orange"),"Naranja")
        tab_widget_2.addTab(Cuadrado("purple"), "Púrpura")
        tab_widget_2.addTab(Cuadrado("pink"), "Rosa")
        tab_widget.addTab(tab_widget_2, "outro")

        tab_widget.setTabPosition(QTabWidget.TabPosition.West)  # Establece la posición de las pestañas en el lateral izquierdo
        tab_widget_2.setTabPosition(QTabWidget.TabPosition.East)

        self.setCentralWidget(tab_widget)

        self.setMinimumSize(400,600)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())