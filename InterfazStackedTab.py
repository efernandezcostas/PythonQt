import sys

from PyQt6.QtWidgets import QMainWindow, QApplication


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()



        self.setMinimumSize(200,200)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec())