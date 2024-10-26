import sys
from PySide6 import QtCore, QtWidgets, QtGui
from logic import Logic

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.logic = Logic()

        self.title = 'Kő-Papír-Olló'
        self.setWindowTitle(self.title)

        self.import_button = QtWidgets.QPushButton("Kép importálása")
        self.evaluate_button = QtWidgets.QPushButton("Kép kiértékelése")
        self.text = QtWidgets.QLabel("Várakozás az inputra...", alignment=QtCore.Qt.AlignCenter)
        

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.import_button)
        self.layout.addWidget(self.evaluate_button)
        self.layout.addWidget(self.text)

        self.import_button.clicked.connect(lambda: self.logic.import_image(self.text)) 
        self.evaluate_button.clicked.connect(lambda: self.logic.evaluate(self.text))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())