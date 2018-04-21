# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialo2.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def setupUi(self, Dialog):
            Dialog.setObjectName("About")
            Dialog.resize(412, 300)
            self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
            self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
            self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
            self.buttonBox.setObjectName("buttonBox")

            textFont_1 = QtGui.QFont("consolas",10, QtGui.QFont.Bold)
            self.textBrowser = QtWidgets.QTextBrowser(Dialog)
            self.textBrowser.setGeometry(QtCore.QRect(40, 40, 300, 180))
            self.textBrowser.setObjectName("textBrowser")
            self.textBrowser.setText("Author:BwZhang.\nDesigned for Computer Programming Ⅱ in spring 2018.")
            self.textBrowser.setFont(textFont_1)

            self.retranslateUi(Dialog)
            self.buttonBox.accepted.connect(Dialog.accept)
            self.buttonBox.rejected.connect(Dialog.reject)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("About", "About"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
