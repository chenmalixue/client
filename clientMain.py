#coding=utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ClientSetting import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
      #  self.pbtok.clicked.connect(self.SaveSetting)
      #  self.pbtok.disconnect()
      #def SaveSetting(self):
       # DBCountValue=""
       # DBAddressValue =""
       # DBPasswordValue =""
       # DBPortValue =""
       # DBtypeValue = self.cbbDBselect.currentText()
       # DBCountValue = self.txtDBCount.text()
       # DBAddressValue = self.txtDBAddress.text()
       # DBPasswordValue = self.txtDBPassword.text()
       # DBPortValue = self.txtDBPort.text()
       # if (DBCountValue and DBAddressValue and DBPortValue and DBPasswordValue == ""):
        #    QMessageBox("MSGBOX")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    #多态
    myshow = MainWindow()
    myshow.show()
    sys.exit(app.exec_())