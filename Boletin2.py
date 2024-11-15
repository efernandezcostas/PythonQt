import sys

from PyQt6.QtWidgets import QMainWindow, QApplication


class Boletin2(QMainWindow):
    def __init__(self):
        super().__init__()



        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Boletin2()
    sys.exit(app.exec())