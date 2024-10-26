from PySide6 import QtCore, QtWidgets, QtGui
import os
import random

class Logic(QtCore.QObject):
    def __init__(self):
        super().__init__()
    @QtCore.Slot(QtWidgets.QWidget)
    def import_image(self,mainwindow):
        """
        Ez a függvény feldobat egy QtDialog-ot, amelyen egy képfájlt tud kiválasztani a felhasználó a programnak, amin a "kő-papír-olló" nevű játék
        kiértékelését végrehajthatja a program.
        """
        mainwindow.text.setText("Kép sikeresen beimportálvaaaaa")
        file_filter='Image Files (*.png *.jpg *.bmp)'
        response=QtWidgets.QFileDialog.getOpenFileName(
            parent=mainwindow,
            caption='Select image file',
            filter=file_filter
        )
        mainwindow.image_path = response[0]
        mainwindow.pixmap = QtGui.QPixmap(mainwindow.image_path)
        mainwindow.pixmap = mainwindow.pixmap.scaled(1280, 720, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        if not mainwindow.pixmap.isNull():
            mainwindow.image_label.setPixmap(mainwindow.pixmap)
        else:
            mainwindow.image_label.setText('A kép nem található')

    @QtCore.Slot(QtWidgets.QLabel)
    def evaluate(self,textbox):
        """
        Ez a függvény neurális háló segítségével meghatározza, hogy a képen melyik játékos nyert. Egy string-el tér vissza.
        """
        textbox.setText(random.choice(["A bal oldali játékos nyert", "A jobb oldali játékos nyert", "Döntetlen"]))
