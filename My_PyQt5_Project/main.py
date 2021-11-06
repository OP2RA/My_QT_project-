import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('Viewform.ui', self)
        self.pushButton.clicked.connect(self.goinside)

    def goinside(self):
        CreateView = Creater()
        widget.addWidget(CreateView)
        widget.setCurrentIndex(widget.CurrentIndex() + 1)
#pyuic5 Creater.ui -o Creater.py

class Creater(QDialog):
    def __init__(self):
        super(Creater, self).__init__()
        loadUi('Creater.ui', self)







app = QApplication(sys.argv)
ex = MyWidget()
widget = QtWidgets.QStackedWidget
#tag.addWidget(welcome)
ex.show()
try:
    sys.exit(app.exec_())
except:
    print('Done')