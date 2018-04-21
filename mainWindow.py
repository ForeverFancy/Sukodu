# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextBrowser,QMessageBox,QLabel
from PyQt5.QtCore import QTimer
import random
import dialog,dialog2,dialog3,ran


class Ui_MainWindow(object):
    def __init__(self,MainWindow):
        self.initialList = [[8, 7, 4, 6, 3, 1, 5, 9, 2],
                            [5, 9, 6, 7, 2, 8, 4, 3, 1],
                            [2, 3, 1, 4, 5, 9, 6, 8, 7],
                            [4, 8, 2, 1, 9, 6, 7, 5, 3],
                            [7, 6, 5, 3, 8, 4, 2, 1, 9],
                            [9, 1, 3, 5, 7, 2, 8, 4, 6],
                            [3, 2, 9, 8, 6, 5, 1, 7, 4],
                            [1, 5, 7, 2, 4, 3, 9, 6, 8],
                            [6, 4, 8, 9, 1, 7, 3, 2, 5]]
        self.second=0
        self.minute=0
        self.hour=0
        self.secondstr='00'
        self.minutestr='00'
        self.hourstr='00'
        self.getList = [[], [], [], [], [], [], [], [], []]
        self.getList_2=[[], [], [], [], [], [], [], [], []]
        self.setupUi(MainWindow=MainWindow)
        self.initialization()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 721, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(9)
        self.tableWidget.resize(455,410)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)   # 隐藏表头

        textFont_1 = QtGui.QFont("微软雅黑", 15, QtGui.QFont.Bold)
        self.label=QLabel(self.centralwidget)
        self.label.resize(100,75)
        self.label.setText("秒表：")
        self.label.move(100,15)
        self.label.setFont(textFont_1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)   #计时器
        self.lineEdit.setGeometry(QtCore.QRect(180, 20, 180, 60))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText('00:00:00')
        self.lineEdit.setFont(textFont_1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        # 设置单元格行款和列宽
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 50)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 50)
        self.tableWidget.setColumnWidth(5, 50)
        self.tableWidget.setColumnWidth(6, 50)
        self.tableWidget.setColumnWidth(7, 50)
        self.tableWidget.setColumnWidth(8, 50)

        self.tableWidget.setItem(0, 0, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu)
        self.menu_4.setObjectName("menu_4")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tuichu = QtWidgets.QAction(MainWindow)
        self.tuichu.setObjectName("tuichu")
        self.actionshengcheng_2 = QtWidgets.QAction(MainWindow)
        self.actionshengcheng_2.setObjectName("actionshengcheng_2")
        self.actionjiandan = QtWidgets.QAction(MainWindow)
        self.actionjiandan.setObjectName("actionjiandan")
        self.actionzhongdeng = QtWidgets.QAction(MainWindow)
        self.actionzhongdeng.setObjectName("actionzhongdeng")
        self.actionkunnan = QtWidgets.QAction(MainWindow)
        self.actionkunnan.setObjectName("actionkunnan")

        self.actionqiujie_2 = QtWidgets.QAction(MainWindow)
        self.actionqiujie_2.setObjectName("actionqiujie_2")



        self.menu_3.addAction(self.actionjiandan)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionzhongdeng)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionkunnan)
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actionqiujie_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.tuichu)
        self.menubar.addAction(self.menu.menuAction())
        self.actionduojiepanduan = QtWidgets.QAction(MainWindow)
        self.actionduojiepanduan.setObjectName("actionduojiepanduan")
        self.actionguanyu = QtWidgets.QAction(MainWindow)
        self.actionguanyu.setObjectName("actionguanyu")
        self.actionguanyu.triggered.connect(lambda :self.msgbox_3())
        self.actionduojiepanduan.triggered.connect(lambda :self.msgbox_4())

        textFont_2 = QtGui.QFont("微软雅黑", 10, QtGui.QFont.Bold)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(90, 580, 112, 34))
        self.pushButton_1.move(450,600)
        self.pushButton_1.setObjectName("submit")
        self.pushButton_1.setText("提交")
        self.pushButton_1.setFont(textFont_2)
        self.pushButton_1.clicked.connect(lambda :(self.stopTime(),self.msgbox()))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 580, 112, 34))
        self.pushButton_2.move(40, 600)
        self.pushButton_2.setObjectName("clean")
        self.pushButton_2.setText("清空")
        self.pushButton_2.setFont(textFont_2)
        self.pushButton_2.clicked.connect(lambda :(self.initialization(),self.resetTime()))


        self.retranslateUi(MainWindow)
        self.tuichu.triggered.connect(MainWindow.close)
        #点击菜单生成
        self.actionjiandan.triggered.connect(lambda :(self.FinalChange(),self.initialization(),self.set_text(1),self.resetTime(),self.beginTime()))
        self.actionzhongdeng.triggered.connect(lambda: (self.FinalChange(),self.initialization(),self.set_text(2),self.resetTime(),self.beginTime()))
        self.actionkunnan.triggered.connect(lambda: (self.FinalChange(),self.initialization(),self.set_text(3),self.resetTime(),self.beginTime()))
        self.actionqiujie_2.triggered.connect(lambda :(self.msgbox_2()))

        self.timerSecond = QTimer()
        self.timerSecond.timeout.connect(lambda: self.update())

        self.menu_2.addAction(self.actionduojiepanduan)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionguanyu)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        textFont = QtGui.QFont("微软雅黑", 10)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu.setFont(textFont)
        self.menu_2.setTitle(_translate("MainWindow", "更多"))
        self.menu_3.setTitle(_translate("MainWindow", "生成"))
        self.menu_4.setTitle(_translate("MainWindow", "求解"))
        self.tuichu.setText(_translate("MainWindow", "退出"))
        self.tuichu.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionshengcheng_2.setText(_translate("MainWindow", "shengcheng"))
        self.actionqiujie_2.setText(_translate("MainWindow", "求解"))
        self.actionjiandan.setText(_translate("MainWindow", "简单"))
        self.actionzhongdeng.setText(_translate("MainWindow", "中等"))
        self.actionkunnan.setText(_translate("MainWindow", "困难"))
        self.actionduojiepanduan.setText(_translate("MainWindow", "多解判断"))
        self.actionduojiepanduan.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionguanyu.setText(_translate("MainWindow", "关于..."))

    def msgbox(self):                                            #判断提交是否成功对话框
        Dialog = QtWidgets.QDialog()
        ui = dialog.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        textFont_1 = QtGui.QFont("consolas", 10, QtGui.QFont.Bold)
        if self.get_Text()==-1:
            ui.textBrowser.setText("Invalid expression.")
            ui.textBrowser.setFont(textFont_1)
        else:
            if self.judge()==True:
                ui.textBrowser.setText("Correct Ansewer!"+'\n'+'Your Time is:'+self.hourstr + ':' + self.minutestr + ':' + self.secondstr)
                ui.textBrowser.setFont(textFont_1)
                self.resetTime()
            else:
                ui.textBrowser.setText("Wrong Ansewer!\nPlease try again!")
                ui.textBrowser.setFont(textFont_1)
                self.beginTime()
        Dialog.exec_()

    def msgbox_2(self):                                              #求解是否成功对话框
        Dialog = QtWidgets.QDialog()
        ui = dialog.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        textFont_1 = QtGui.QFont("consolas", 10, QtGui.QFont.Bold)#先求解，求解之后判断解是否合理，不合理报错。
        if self.get_Text()==-1:
            ui.textBrowser.setText("Invalid expression.")
            ui.textBrowser.setFont(textFont_1)
        else:
            self.start()
            if self.judge_2():
                self.set_Text2()
                ui.textBrowser.setText("The problem has been solved!\n")
                ui.textBrowser.setFont(textFont_1)

            else:
                ui.textBrowser.setText("The problem has no solution!")
                ui.textBrowser.setFont(textFont_1)
        Dialog.exec_()

    def msgbox_3(self):                                            #作者对话框
        Dialog = QtWidgets.QDialog()
        ui = dialog2.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def msgbox_4(self):                                             #难度对话框
        Dialog = QtWidgets.QDialog()
        ui = dialog3.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        textFont_1 = QtGui.QFont("consolas", 10, QtGui.QFont.Bold)
        self.get_Text()
        k = self.judge_3()
        if k == 1:
            ui.textBrowser.setText("The problem only have one solution.")
            ui.textBrowser.setFont(textFont_1)
        elif k > 1:
            ui.textBrowser.setText("The problem have "+str(k)+" solutions.")
            ui.textBrowser.setFont(textFont_1)
        Dialog.exec_()

    def initialization(self):                                 #初始化，并在必要的地方加上颜色
        for i in range(0,3):
            for j in range(0,3):
                item = QtWidgets.QTableWidgetItem(" ")
                item.setBackground(QtGui.QColor(240,255,240))
                self.tableWidget.setItem(i, j, item)

        for i in range(0,3):
            for j in range(3,6):
                item = QtWidgets.QTableWidgetItem(" ")
                self.tableWidget.setItem(i, j, item)

        for i in range(0,3):
            for j in range(6,9):
                item = QtWidgets.QTableWidgetItem(" ")
                item.setBackground(QtGui.QColor(240, 255, 240))
                self.tableWidget.setItem(i, j, item)

        for i in range(3,6):
            for j in range(0,3):
                item = QtWidgets.QTableWidgetItem(" ")
                self.tableWidget.setItem(i, j, item)

        for i in range(3,6):
            for j in range(3,6):
                item = QtWidgets.QTableWidgetItem(" ")
                item.setBackground(QtGui.QColor(240, 255, 240))
                self.tableWidget.setItem(i, j, item)

        for i in range(3,6):
            for j in range(6,9):
                item = QtWidgets.QTableWidgetItem(" ")
                self.tableWidget.setItem(i, j, item)

        for i in range(6,9):
            for j in range(0,3):
                item = QtWidgets.QTableWidgetItem(" ")
                item.setBackground(QtGui.QColor(240,255,240))
                self.tableWidget.setItem(i, j, item)

        for i in range(6,9):
            for j in range(3,6):
                item = QtWidgets.QTableWidgetItem(" ")
                self.tableWidget.setItem(i, j, item)

        for i in range(6,9):
            for j in range(6,9):
                item = QtWidgets.QTableWidgetItem(" ")
                item.setBackground(QtGui.QColor(240, 255, 240))
                self.tableWidget.setItem(i, j, item)

    def set_text(self,dif):
        if dif==1:
            for i in range(9):
                for j in range(9):
                    if (i in range(0,3) and (j in range(0,3) or j in range(6,9))) or (i in range(6,9) and (j in range(0,3) or j in range(6,9))) or (i in range(3,6) and j in range(3,6)):
                        item=QtWidgets.QTableWidgetItem(" ")
                        item.setBackground(QtGui.QColor(240, 255, 240))
                        self.tableWidget.setItem(i,j,item)
            for i in range(9):
                randomList=random.sample(range(0,9),3)
                for j in range(9):
                    if j not in randomList:
                        if (i in range(0, 3) and (j in range(0, 3) or j in range(6, 9))) or (
                                i in range(6, 9) and (j in range(0, 3) or j in range(6, 9))) or (
                                i in range(3, 6) and j in range(3, 6)):
                            item=QtWidgets.QTableWidgetItem(str(self.initialList[i][j]))
                            item.setBackground(QtGui.QColor(240, 255, 240))
                            self.tableWidget.setItem(i,j,item)
                        else:
                            item = QtWidgets.QTableWidgetItem(str(self.initialList[i][j]))
                            self.tableWidget.setItem(i, j, item)
            self.get_Text()
            if self.judge_3()>1:
                self.set_text(1)


        elif dif==2:
            for i in range(9):
                for j in range(9):
                    if (i in range(0,3) and (j in range(0,3) or j in range(6,9))) or (i in range(6,9) and (j in range(0,3) or j in range(6,9))) or (i in range(3,6) and j in range(3,6)):
                        item=QtWidgets.QTableWidgetItem(" ")
                        item.setBackground(QtGui.QColor(240, 255, 240))
                        self.tableWidget.setItem(i,j,item)
            for i in range(9):
                randomList=random.sample(range(0,9),5)
                for j in range(9):
                    if j not in randomList:
                        if (i in range(0, 3) and (j in range(0, 3) or j in range(6, 9))) or (
                                i in range(6, 9) and (j in range(0, 3) or j in range(6, 9))) or (
                                i in range(3, 6) and j in range(3, 6)):
                            item=QtWidgets.QTableWidgetItem(str(self.initialList[i][j]))
                            item.setBackground(QtGui.QColor(240, 255, 240))
                            self.tableWidget.setItem(i,j,item)
                        else:
                            item = QtWidgets.QTableWidgetItem(str(self.initialList[i][j]))
                            self.tableWidget.setItem(i, j, item)
            self.get_Text()
            if self.judge_3() > 1:
                self.initialization()
                self.set_text(2)
        elif dif==3:
            for i in range(9):
                for j in range(9):
                    if (i in range(0,3) and (j in range(0,3) or j in range(6,9))) or (i in range(6,9) and (j in range(0,3) or j in range(6,9))) or (i in range(3,6) and j in range(3,6)):
                        item=QtWidgets.QTableWidgetItem(" ")
                        item.setBackground(QtGui.QColor(240, 255, 240))
                        self.tableWidget.setItem(i,j,item)
            for i in range(9):
                randomList=random.sample(range(0,9),7)
                for j in range(9):
                    if j not in randomList:
                        if (i in range(0, 3) and (j in range(0, 3) or j in range(6, 9))) or (
                                i in range(6, 9) and (j in range(0, 3) or j in range(6, 9))) or (
                                i in range(3, 6) and j in range(3, 6)):
                            item=QtWidgets.QTableWidgetItem(str(self.initialList[i][j]))
                            item.setBackground(QtGui.QColor(240, 255, 240))
                            self.tableWidget.setItem(i,j,item)
                        else:
                            item = QtWidgets.QTableWidgetItem(str(self.initialList[i][j]))
                            self.tableWidget.setItem(i, j, item)
            self.get_Text()
            if self.judge_3() > 1:
                self.initialization()
                self.set_text(3)

    def get_Text(self):
        self.getList = [[], [], [], [], [], [], [], [], []]
        self.getList_2 = [[], [], [], [], [], [], [], [], []]
        for i in range(9):
            for j in range(9):
                if self.tableWidget.item(i,j).text()<='9' and self.tableWidget.item(i,j).text()>='1':
                    self.getList[i].append(int(self.tableWidget.item(i,j).text()))
                    self.getList_2[i].append(int(self.tableWidget.item(i, j).text()))
                elif self.tableWidget.item(i,j).text()==' ':
                    self.getList[i].append(0)
                    self.getList_2[i].append(0)
                else :
                    return -1

    def ChangeValue(self,List, before, after):
        for i in range(9):
            for j in range(9):
                if List[i][j] == before:
                    List[i][j] = after
                elif List[i][j] == after:
                    List[i][j] = before

    def Change1(self,List):
        for i in range(10):  # 10 could be other number
            m = random.randint(1, 9)
            n = random.randint(1, 9)
            if m != n:
                self.ChangeValue(List, m, n)
            else:
                m -= 1

    def ChangeRow(self,List, before, after):
        temp = []
        temp.append(List[before])
        List[before] = List[after]
        List[after] = temp[0]

    def ChangeCol(self,List, before, after):
        for i in range(9):
            for j in range(9):
                if j == before:
                    temp = List[i][j]
                    List[i][j] = List[i][after]
                    List[i][after] = temp

    def Change2(self,List):

        for i in range(10):
            m = random.randint(0, 2)
            n = random.randint(0, 2)
            if m != n:
                self.ChangeCol(List, m, n)
            m = random.randint(0, 2)
            n = random.randint(0, 2)
            if m != n:
                self.ChangeRow(List, m, n)

        for i in range(10):
            m = random.randint(3, 5)
            n = random.randint(3, 5)
            if m != n:
                self.ChangeRow(List, m, n)
            m = random.randint(3, 5)
            n = random.randint(3, 5)
            if m != n:
                self.ChangeCol(List, m, n)

            for i in range(10):
                m = random.randint(6, 8)
                n = random.randint(6, 8)
                if m != n:
                    self.ChangeCol(List, m, n)
                m = random.randint(6, 8)
                n = random.randint(6, 8)
                if m != n:
                    self.ChangeRow(List, m, n)

    def ChangeThreeRow(self,List, before, after):
        for i in range(3):
            self.ChangeRow(List, before + i, after + i)

    def ChangeThreeCol(self,List, before, after):
        for i in range(3):
            self.ChangeCol(List, before + i, after + i)

    def Change3(self,List):
        for i in range(10):
            m = 3 * random.randint(0, 2)
            n = 3 * random.randint(0, 2)
            if m != n:
                self.ChangeThreeCol(List, m, n)
        for i in range(10):
            m = 3 * random.randint(0, 2)
            n = 3 * random.randint(0, 2)
            if m != n:
                self.ChangeThreeRow(List, m, n)

    def FinalChange(self):
        self.Change1(self.initialList)
        self.Change2(self.initialList)
        self.Change3(self.initialList)

    def judge(self):                                   #检查是否符合规则
        for i in range(0,9):
            for j in range(0,9):
                if self.check(i,j,self.getList[i][j])==False or self.getList[i][j]==0:
                    return False
        return True

    def judge_2(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.check(i,j,self.getList_2[i][j])==False or self.getList_2[i][j]==0:
                    return False
        return True

    def check(self,x,y,value):                                      #检查所在行列和九宫格内有没有相同的数字

        for j in range(0,9):
            if j!=y:
                if self.getList_2[x][j] == value:
                    return False

        for i in range(0,9):
            if i!=x:
                if self.getList_2[i][y] == value:
                    return False

        row, col = int(x/3)*3, int(y/3)*3
        for i in range(row,row+3):
            for j in range(col,col+3):
                if i!=x and j!=y :
                    if self.getList_2[i][j]==value:
                        return False

        return True

    def getNext(self,x,y):

        for j in range(y+1,9):
            if self.getList_2[x][j]==0:
                return x,j

        for i in range(x+1,9):
            for j in range(0,9):
                if self.getList_2[i][j]==0:
                    return i,j
        return -1,-1

    def tryIt(self,x,y):
        if self.getList_2[x][y]==0:
            for i in range(1,10):
                if self.check(x,y,i):
                    self.getList_2[x][y]=i
                    next_x,next_y=self.getNext(x,y)
                    if next_x==-1:
                        return True
                    else:
                        end=self.tryIt(next_x,next_y)
                        if not end:
                            self.getList_2[x][y]=0
                        else:
                            return True

    def start(self):
        if self.get_Text()!=-1:
            for i in range(0,9):
                for j in range(0,9):
                    if self.getList_2[i][j] ==0:
                        self.tryIt(i,j)

    def set_Text2(self):
        textFont = QtGui.QFont("微软雅黑", 15, QtGui.QFont.Bold)          # 求解填入的数字字体
        for i in range(0,9):
            for j in range(0,9):
                if self.getList[i][j]==0:
                    if (i in range(0, 3) and (j in range(0, 3) or j in range(6, 9))) or (
                            i in range(6, 9) and (j in range(0, 3) or j in range(6, 9))) or (
                            i in range(3, 6) and j in range(3, 6)):
                        item = QtWidgets.QTableWidgetItem(str(self.getList_2[i][j]))
                        item.setFont(textFont)
                        item.setBackground(QtGui.QColor(240, 255, 240))
                        self.tableWidget.setItem(i, j, item)
                    else:
                        item = QtWidgets.QTableWidgetItem(str(self.getList_2[i][j]))
                        item.setFont(textFont)
                        self.tableWidget.setItem(i, j, item)

    def beginTime(self):
        textFont = QtGui.QFont("微软雅黑", 15, QtGui.QFont.Bold)
        self.lineEdit.setText("00:00:00")
        self.lineEdit.setFont(textFont)
        self.timerSecond.start(1000)

    def update(self):                                           #时间更新
        textFont = QtGui.QFont("微软雅黑", 15, QtGui.QFont.Bold)
        self.second=self.second+1

        if self.second==60:
            self.second=0
            if self.minute<60:
                self.minute+=1

            if self.minute==60:
                self.minute=0
                self.hour+=1

        if self.hour<10:
            self.hourstr='0'+str(self.hour)
        else:
            self.hourstr=str(self.hour)

        if self.minute<10:
            self.minutestr='0'+str(self.minute)
        else:
            self.minutestr=str(self.minute)

        if self.second<10:
            self.secondstr='0'+str(self.second)
        else:
            self.secondstr=str(self.second)

        self.lineEdit.setText(self.hourstr + ':' + self.minutestr + ':' + self.secondstr)
        self.lineEdit.setFont(textFont)

    def stopTime(self):
        self.timerSecond.stop()

    def resetTime(self):                                                     #重置时间
        textFont = QtGui.QFont("微软雅黑", 15, QtGui.QFont.Bold)
        self.lineEdit.setText("00:00:00")
        self.lineEdit.setFont(textFont)

        self.timerSecond.stop()

        self.hour=0
        self.minute=0
        self.second=0

    def difficultyJudge(self):                                   #难度判断，根据每个空格的自由度，所在行列和九宫格内还有多少空格
        self.get_Text()
        sum = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if self.getList[i][j] == 0:
                    for k in range(0, 9):
                        if k != j and self.getList[i][k] == 0:
                            sum += 1
                    for k in range(0, 9):
                        if k != i and self.getList[k][j] == 0:
                            sum += 1
                    row, col = int(i / 3) * 3, int(j / 3) * 3
                    for m in range(row, row + 3):
                        for n in range(col, col + 3):
                            if m != i and n != j:
                                if self.getList[m][n] == 0:
                                    sum += 1
        if sum<=300:
            return 1
        elif sum>300 and sum<=600:
            return 2
        else:
            return 3

    def judge_3(self):
        su=ran.sukudo(self.getList_2)
        su.start()
        for i in range(0,9):
            for j in range(0,9):
                self.getList_2[i][j]=self.getList[i][j]
        return su.count



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
