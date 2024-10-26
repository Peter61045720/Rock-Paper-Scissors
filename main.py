import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Kő-Papír-Olló'
        self.setWindowTitle(self.title)

        self.import_button = QtWidgets.QPushButton("Kép importálása")
        self.evaluate_button = QtWidgets.QPushButton("Kép kiértékelése")
        self.text = QtWidgets.QLabel("Várakozás az inputra...", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.text)

        self.button1.clicked.connect(self.import_image)
        self.button2.clicked.connect(self.evaluate)

    @QtCore.Slot()
    def import_image(self):
        self.text.setText("Kép sikeresen beimportálva")

    @QtCore.Slot()
    def evaluate(self):
        self.text.setText(random.choice(["A bal oldali játékos nyert", "A jobb oldali játékos nyert", "Döntetlen"]))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())