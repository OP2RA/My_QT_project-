from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1034, 754)
        self.view = QtWidgets.QWidget(Dialog)
        self.view.setGeometry(QtCore.QRect(0, 0, 1041, 751))
        self.view.setStyleSheet("QWidget#view{\n"
                                "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.00568182, "
                                "stop:0 rgba(0, 0, 0, 255), stop:1 rgba(54, 54, 54, 255))}")
        self.view.setObjectName("view")
        self.tabWidget = QtWidgets.QTabWidget(self.view)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1041, 761))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.view_2 = QtWidgets.QWidget(self.tab)
        self.view_2.setGeometry(QtCore.QRect(0, 0, 1041, 751))
        self.view_2.setStyleSheet("QWidget#view_2{\n"
                                  "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.00568182, "
                                  "stop:0 rgba(0, 0, 0, 255), stop:1 rgba(54, 54, 54, 255))}")
        self.view_2.setObjectName("view_2")
        self.progressBar = QtWidgets.QProgressBar(self.view_2)
        self.progressBar.setGeometry(QtCore.QRect(20, 690, 531, 23))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(self.view_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 120, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.view_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 411, 71))
        self.label.setStyleSheet("color: rgb(0, 152, 0);\n"
                                 "font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.view_2)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 91, 71))
        self.label_2.setStyleSheet("color: rgb(0, 247, 119);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.view_2)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 91, 71))
        self.label_3.setStyleSheet("color: rgb(0, 247, 119);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.view_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 170, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.view_2)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 91, 71))
        self.label_4.setStyleSheet("color: rgb(0, 247, 119);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.view_2)
        self.comboBox.setGeometry(QtCore.QRect(90, 221, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Give settings to your pazzle"))
        self.label_2.setText(_translate("Dialog", "Length :"))
        self.label_3.setText(_translate("Dialog", "Width :"))
        self.label_4.setText(_translate("Dialog", "Color :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
