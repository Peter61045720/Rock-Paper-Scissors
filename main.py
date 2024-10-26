import sys
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Kő-Papír-Olló'
        self.setWindowTitle(self.title)

        self.import_button = QtWidgets.QPushButton('Kép importálása')
        self.evaluate_button = QtWidgets.QPushButton('Kép kiértékelése')
        self.text = QtWidgets.QLabel('Várakozás az inputra...', alignment=QtCore.Qt.AlignCenter)

        self.image_label = QtWidgets.QLabel(self, alignment=QtCore.Qt.AlignCenter)
        self.image_path = 'test_image.png'
        self.pixmap = QtGui.QPixmap(self.image_path)
        if not self.pixmap.isNull():
            self.image_label.setPixmap(self.pixmap)
        else:
            self.image_label.setText('A kép nem található')
        self.resize(self.pixmap.width(), self.pixmap.height())

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.import_button)
        self.layout.addWidget(self.evaluate_button)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())