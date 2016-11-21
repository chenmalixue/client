#coding=utf-8

import os,sys
import MySQLdb
from PyQt5.QtWidgets import QMessageBox
#class DataInsert():


#class DataAlter():




#class DataRead():



class SignalSlotClientSettingPbtok():


    def msg(self):
        OK = QMessageBox.information(self, ("这是标题"), ("""这是信息框"""),QMessageBox.StandardButton(QMessageBox.Yes | QMessageBox.No))