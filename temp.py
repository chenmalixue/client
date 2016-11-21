# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/cx/ClientSetting.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DBconnect
from DBconnect import SignalSlotClientSettingPbtok

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gbxDBSetting = QtWidgets.QGroupBox(self.centralwidget)
        self.gbxDBSetting.setGeometry(QtCore.QRect(10, 10, 781, 211))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gbxDBSetting.setFont(font)
        self.gbxDBSetting.setToolTipDuration(0)
        self.gbxDBSetting.setObjectName("gbxDBSetting")
        self.label = QtWidgets.QLabel(self.gbxDBSetting)
        self.label.setGeometry(QtCore.QRect(60, 70, 90, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.gbxDBSetting)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 90, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.gbxDBSetting)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 90, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.gbxDBSetting)
        self.label_4.setGeometry(QtCore.QRect(410, 110, 90, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.gbxDBSetting)
        self.label_5.setGeometry(QtCore.QRect(410, 150, 90, 30))
        self.label_5.setObjectName("label_5")
        self.cbbDBselect = QtWidgets.QComboBox(self.gbxDBSetting)
        self.cbbDBselect.setGeometry(QtCore.QRect(140, 70, 200, 30))
        self.cbbDBselect.setObjectName("cbbDBselect")
        self.cbbDBselect.addItem("")
        self.cbbDBselect.addItem("")
        self.cbbDBselect.addItem("")
        self.cbbDBselect.addItem("")
        self.txtDBCount = QtWidgets.QLineEdit(self.gbxDBSetting)
        self.txtDBCount.setGeometry(QtCore.QRect(140, 110, 200, 30))
        self.txtDBCount.setObjectName("txtDBCount")
        self.txtDBPassword = QtWidgets.QLineEdit(self.gbxDBSetting)
        self.txtDBPassword.setGeometry(QtCore.QRect(140, 150, 200, 30))
        self.txtDBPassword.setObjectName("txtDBPassword")
        self.txtDBAddress = QtWidgets.QLineEdit(self.gbxDBSetting)
        self.txtDBAddress.setGeometry(QtCore.QRect(490, 110, 200, 30))
        self.txtDBAddress.setObjectName("txtDBAddress")
        self.txtDBPort = QtWidgets.QLineEdit(self.gbxDBSetting)
        self.txtDBPort.setGeometry(QtCore.QRect(490, 150, 200, 30))
        self.txtDBPort.setObjectName("txtDBPort")
        self.pbtok = QtWidgets.QPushButton(self.centralwidget)
        self.pbtok.setGeometry(QtCore.QRect(210, 490, 115, 32))
        self.pbtok.setObjectName("pbtok")
        self.pbtcancel = QtWidgets.QPushButton(self.centralwidget)
        self.pbtcancel.setGeometry(QtCore.QRect(480, 490, 115, 32))
        self.pbtcancel.setObjectName("pbtcancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
      #  self.pbtok.clicked.connect(DBconnect.SignalSlotClientSettingPbtok)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gbxDBSetting.setTitle(_translate("MainWindow", "数据库配置"))
        self.label.setText(_translate("MainWindow", "数据库类型："))
        self.label_2.setText(_translate("MainWindow", "数据库账户："))
        self.label_3.setText(_translate("MainWindow", "数据库密码："))
        self.label_4.setText(_translate("MainWindow", "数据库地址："))
        self.label_5.setText(_translate("MainWindow", "数据库端口："))
        self.cbbDBselect.setItemText(0, _translate("MainWindow", "MySQL"))
        self.cbbDBselect.setItemText(1, _translate("MainWindow", "Oracle"))
        self.cbbDBselect.setItemText(2, _translate("MainWindow", "SQLite"))
        self.cbbDBselect.setItemText(3, _translate("MainWindow", "SQLServer"))
        self.pbtok.setText(_translate("MainWindow", "确定"))
        self.pbtcancel.setText(_translate("MainWindow", "清除"))

