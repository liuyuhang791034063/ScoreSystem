# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sblogin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_afui(object):
    def setupUi(self, afui):
        afui.setObjectName("afui")
        afui.resize(404, 144)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        afui.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(afui)
        self.label.setGeometry(QtCore.QRect(150, 40, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(afui)
        self.pushButton.setGeometry(QtCore.QRect(80, 90, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(afui)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 90, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(afui)
        QtCore.QMetaObject.connectSlotsByName(afui)

    def retranslateUi(self, afui):
        _translate = QtCore.QCoreApplication.translate
        afui.setWindowTitle(_translate("afui", "登陆失败"))
        self.label.setText(_translate("afui", "是否重新登陆"))
        self.pushButton.setText(_translate("afui", "重新登陆"))
        self.pushButton_2.setText(_translate("afui", "取消"))

