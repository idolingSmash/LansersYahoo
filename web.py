import sys
import urllib.request, urllib.error
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from bs4 import BeautifulSoup

# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.initUI()

    def initUI(self):
        self.iLabel = QtGui.QLabel("Query List",self)
        self.iLabel.move(50,25)
        self.iText = QtGui.QTextEdit(self)
        self.iText.setGeometry(50,50,200,500)
        self.arrowLabel = QtGui.QLabel("→",self)
        self.arrowLabel.move(260,300)
        self.arrowFont = QtGui.QFont()
        self.arrowFont.setPointSize(20)
        self.arrowLabel.setFont(self.arrowFont)
        self.oLabel = QtGui.QLabel("Result List",self)
        self.oLabel.move(300,25)
        self.oText = QtGui.QTextEdit(self)
        self.oText.setGeometry(300,50,400,500)

        self.initRankUI() # set radio button

        self.submitBtn = QtGui.QPushButton("Submit", self);
        self.submitBtn.move(750, 450)
        self.submitBtn.clicked.connect(self.btnSubmit)

        # x and y coordinates on the screen, width, height
        self.setGeometry(50,50,900,650)
        self.setWindowTitle("Web Scraping(Yahoo.co.jp)")

    def initRankUI(self):
        #set Back-Ground Color
        self.palette = QtGui.QPalette();
        self.palette.setColor(QtGui.QPalette.Background, QtGui.QColor(147,184,129))

        self.RW = QtGui.QWidget(self)
        self.btn1 = QtGui.QRadioButton("Rank1",self.RW)
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda:self.btnstate(self.btn1))
        self.btn2 = QtGui.QRadioButton("Rank2",self.RW)
        self.btn2.toggled.connect(lambda:self.btnstate(self.btn2))
        self.btn3 = QtGui.QRadioButton("Rank3",self.RW)
        self.btn3.toggled.connect(lambda:self.btnstate(self.btn3))
        self.btn4 = QtGui.QRadioButton("Rank4",self.RW)
        self.btn4.toggled.connect(lambda:self.btnstate(self.btn4))
        self.btn5 = QtGui.QRadioButton("Rank5",self.RW)
        self.btn5.toggled.connect(lambda:self.btnstate(self.btn5))
        self.btn6 = QtGui.QRadioButton("Rank6",self.RW)
        self.btn6.toggled.connect(lambda:self.btnstate(self.btn6))
        self.btn7 = QtGui.QRadioButton("Rank7",self.RW)
        self.btn7.toggled.connect(lambda:self.btnstate(self.btn7))
        self.btn8 = QtGui.QRadioButton("Rank8",self.RW)
        self.btn8.toggled.connect(lambda:self.btnstate(self.btn8))
        self.btn9 = QtGui.QRadioButton("Rank9",self.RW)
        self.btn9.toggled.connect(lambda:self.btnstate(self.btn9))
        self.btn10 = QtGui.QRadioButton("Rank10",self.RW)
        self.btn10.toggled.connect(lambda:self.btnstate(self.btn10))

        self.RW.setAutoFillBackground(True)
        self.RW.setPalette(self.palette)

        self.btn1.move(0, 0)
        self.btn2.move(0, 20)
        self.btn3.move(0, 40)
        self.btn4.move(0, 60)
        self.btn5.move(0, 80)
        self.btn6.move(0, 100)
        self.btn7.move(0, 120)
        self.btn8.move(0, 140)
        self.btn9.move(0, 160)
        self.btn10.move(0, 180)    	    	
        self.RW.setGeometry(750,200,80,200)

    def btnstate(self, btn):
        if btn.isChecked() == True:
            print(btn.text())

    def rankChecker(self):
        rank = 0
        if self.btn1.isChecked():
            rank = 1
        elif self.btn2.isChecked():
            rank = 2
        elif self.btn3.isChecked():
            rank = 3
        elif self.btn4.isChecked():
            rank = 4
        elif self.btn5.isChecked():
            rank = 5
        elif self.btn6.isChecked():
            rank = 6
        elif self.btn7.isChecked():
            rank = 7
        elif self.btn8.isChecked():
            rank = 8
        elif self.btn9.isChecked():
            rank = 9
        elif self.btn10.isChecked():
            rank = 10
        return rank

    def btnSubmit(self):
        yahooURL = "http://search.yahoo.co.jp/search?p=";
        qlist = self.iText.toPlainText().split('\n')
        self.resultList = []
        resultStr = ""
        for query in qlist:        
            qURL = yahooURL + urllib.request.quote(query)
            html = urllib.request.urlopen(qURL).read()
            soup = BeautifulSoup(html, "html.parser")
            f = soup.find_all("a")


            idx = -1
            for t in f:
                idx = idx + 1
                if t.string is not None: 
                    if t.text in "この検索結果ページについて":
                        break

            qa = f[idx+1:]
            if 0 < self.rankChecker():
                self.resultList.append(qa[self.rankChecker()-1].get("href"))

        for item in self.resultList:
            resultStr = resultStr + item + "\n"

        self.oText.setText(resultStr)


def main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
