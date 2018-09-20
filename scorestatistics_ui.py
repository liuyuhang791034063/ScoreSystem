# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scorestatistics.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Score(object):
    def setupUi(self, Score):
        Score.setObjectName("Score")
        Score.resize(537, 412)
        self.tableWidget = QtWidgets.QTableWidget(Score)
        self.tableWidget.setGeometry(QtCore.QRect(50, 110, 421, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Score)
        self.label.setGeometry(QtCore.QRect(40, 50, 461, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Score)
        QtCore.QMetaObject.connectSlotsByName(Score)

    def retranslateUi(self, Score):
        _translate = QtCore.QCoreApplication.translate
        Score.setWindowTitle(_translate("Score", "成绩统计"))
        self.label.setText(_translate("Score", "TextLabel"))

