import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog


class MainScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1041, 730)
        loadUi('Viewform.ui', self)
        self.pushButton.clicked.connect(self.goinside)
        self.pushButton_2.clicked.connect(self.getFileNames)

    def getFileNames(self):
        filenames = QFileDialog.getOpenFileNames(self, '', '.')
        return filenames[0][0]


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
        try:
            filenames = QFileDialog.getOpenFileNames(self, '', '.')
            self.folder = filenames[0][0]
            if str(self.folder[len(self.folder) - 3:]) != 'png':
                raise ImportError
            else:
                self.image = QPixmap(self.folder)
                self.label.setPixmap(self.image)

        except ImportError:
            self.err = Error()
            self.err.show()

    def yourPhoto(self, name):
        return name

    def start(self):
        import pygame_front

    def returnWid(self):
        self.returnView = MainScreen()
        self.returnView.show()
        self.hide()

class Error(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('error_notific.ui', self)
        self.pushButton.clicked.connect(self.hidewid)
    def hidewid(self):
        self.hide()





def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainScreen()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())



