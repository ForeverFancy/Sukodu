from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def setupUi(self, Dialog):
            Dialog.setObjectName("DifficultyJudge")
            Dialog.resize(412, 240)
            self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
            self.buttonBox.setGeometry(QtCore.QRect(30, 180, 341, 32))
            self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
            self.buttonBox.setObjectName("buttonBox")

            textFont_1 = QtGui.QFont("consolas",10, QtGui.QFont.Bold)
            self.textBrowser = QtWidgets.QTextBrowser(Dialog)
            self.textBrowser.setGeometry(QtCore.QRect(60, 40, 300, 100))
            self.textBrowser.setObjectName("textBrowser")
            self.textBrowser.setFont(textFont_1)

            self.retranslateUi(Dialog)
            self.buttonBox.accepted.connect(Dialog.accept)
            self.buttonBox.rejected.connect(Dialog.reject)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("solutionJudge", "solutionJudge"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())