from PySide6 import QtCore, QtWidgets, QtGui
## A képfeldolgozós részhez opencv kell, illetve a numpy és a matplotlib könyvtárak is.
## pip install opencv-python|matplotlib (a numpy az opencv-vel együtt települ.)
## Tensorflow is szükséges a működéshez.
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras

class Logic(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.model = keras.models.load_model("./model/baseline_cnn_model.keras")
        self.model.summary()
    @QtCore.Slot(QtWidgets.QWidget)
    def import_image(self,mainwindow):
        """
        Ez a függvény feldobat egy QFileDialog-ot, amelyen egy képfájlt tud kiválasztani a felhasználó a programnak, amin a "kő-papír-olló" nevű játék
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
    def evaluate(self,mainwindow):
        """
        Ez a függvény neurális háló segítségével meghatározza, hogy a képen melyik játékos nyert. Egy string-el tér vissza.
        """

        img = cv.imread(mainwindow.image_path)

        if img is None:
            dlg = QtWidgets.QMessageBox(mainwindow)
            dlg.setWindowTitle("Hiba")
            dlg.setText("A kép nem található.")
            dlg.exec()
            return
        
        
        # Itt vágjuk kétfelé a közepénél a képet
        img_firsthalf = img[:,:int(img.shape[1]/2),:]
        img_secondhalf = img[:,int(img.shape[1]/2):int(img.shape[1]),:]

        # Plotolas 
        resized_firstpart = cv.resize(img_firsthalf, (320, 240))
        resized_secondpart = cv.resize(img_secondhalf, (320, 240))
        img_rgb = cv.cvtColor(resized_firstpart, cv.COLOR_BGR2RGB)
        img_rgb2 = cv.cvtColor(resized_secondpart, cv.COLOR_BGR2RGB)
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        fig.suptitle('A megjátszott kezek:')
        axs[0].imshow(img_rgb)
        axs[0].set_title('Bal oldali játékos')
        axs[1].imshow(img_rgb2)
        axs[1].set_title('Jobb oldali játékos')
        fig.tight_layout()
        plt.show()

        # Normalizalas a neuralis halon valo felismeresehez
        normalized_firsthalf = self.normalize_image(img_firsthalf)
        normalized_secondhalf = self.normalize_image(img_secondhalf)

        res1 = self.model.predict(normalized_firsthalf)
        res2 = self.model.predict(normalized_secondhalf)
        print(res1)
        print(res2)
        
        

        #TODO ha ez megtörtént, a függvény utolsó része az, hogy lekódoljuk a 9 esetet a felismerés alapján, és visszatérjünk egy stringgel.


    def normalize_image(self, image):
        normalized_image = cv.resize(image, (300, 300))
        normalized_image = cv.cvtColor(normalized_image, cv.COLOR_BGR2RGB)
        normalized_image = normalized_image.astype("float32") / 255.0
        normalized_image = np.expand_dims(normalized_image, axis=0)
        return normalized_image
    