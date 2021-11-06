from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1034, 754)
        self.view = QtWidgets.QWidget(Dialog)
        self.view.setGeometry(QtCore.QRect(0, 0, 1041, 751))
        self.view.setStyleSheet("QWidget#view{\n"
                                "background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:"
                                "0 rgba(127, 0, 191, 255), stop:1 rgba(59, 227, 206, 255));}")
        self.view.setObjectName("view")
        self.label = QtWidgets.QLabel(self.view)
        self.label.setGeometry(QtCore.QRect(310, 70, 391, 111))
        self.label.setStyleSheet("font: 28pt \"Myanmar Text\"; color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.view)
        self.pushButton.setGeometry(QtCore.QRect(330, 310, 321, 51))
        self.pushButton.setStyleSheet("border-radius: 20px;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0.228856, y1:0.46, x2:1, y2:1, "
                                      "stop:0 rgba(170, 0, 0, 255), stop:1 rgba(255, 227, 170, 255));\n"
                                      "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                      "color: rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.view)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 410, 321, 51))
        self.pushButton_2.setStyleSheet("border-radius: 20px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.228856, y1:0.46, x2:1, "
                                        "y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(255, 227, 170, 255));\n"
                                        "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255, 255, 255)")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose your way"))
        self.pushButton.setText(_translate("Dialog", "Create"))
        self.pushButton_2.setText(_translate("Dialog", "Download"))
