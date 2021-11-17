import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
#from PyGame import Pazzle

import pygame_front

global folder
class MainScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1041, 730)
        loadUi('Viewform.ui', self)
        self.pushButton.clicked.connect(self.goinside)
        self.pushButton_2.clicked.connect(self.getFileNames)

    def getFileNames(self):
        filenames = QFileDialog.getOpenFileNames(self, '', '.')
        self.folder = filenames


    def goinside(self):
        self.CreateView = Creater()
        self.CreateView.show()
        self.hide()



class Creater(MainScreen):
    def __init__(self):
        super(Creater, self).__init__()

        loadUi('Creater_1.ui', self)
        self.pushButton.clicked.connect(self.returnWid)
        self.pushButton_2.clicked.connect(self.showphoto)
        self.pushButton_4.clicked.connect(self.start)

    def showphoto(self):
        filenames = QFileDialog.getOpenFileNames(self, '', '.')
        self.folder = filenames
        image = QPixmap(self.folder[0][0])
        self.label_5.setPixmap(image)

    def start(self):
        pygame_front.start_game()


    def returnWid(self):
        self.returnView = MainScreen()
        self.returnView.show()
        self.hide()





def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainScreen()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())



