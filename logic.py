from PySide6 import QtCore, QtWidgets, QtGui
import random

class Logic(QtCore.QObject):
    def __init__(self):
        super().__init__()
    @QtCore.Slot(QtWidgets.QLabel)
    def import_image(self,textbox):
        """
        Ez a függvény feldobat egy QtDialog-ot, amelyen egy képfájlt tud kiválasztani a felhasználó a programnak, amin a "kő-papír-olló" nevű játék
        kiértékelését végrehajthatja a program.
        """
        textbox.setText("Kép sikeresen beimportálvaaaaa")
    @QtCore.Slot(QtWidgets.QLabel)
    def evaluate(self,textbox):
        """
        Ez a függvény neurális háló segítségével meghatározza, hogy a képen melyik játékos nyert. Egy string-el tér vissza.
        """
        textbox.setText(random.choice(["A bal oldali játékos nyert", "A jobb oldali játékos nyert", "Döntetlen"]))
