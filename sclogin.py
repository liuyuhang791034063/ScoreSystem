# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sclogin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_scui(object):
    def setupUi(self, scui):
        scui.setObjectName("scui")
        scui.resize(404, 144)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        scui.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(scui)
        self.label.setGeometry(QtCore.QRect(130, 30, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(scui)
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(scui)
        QtCore.QMetaObject.connectSlotsByName(scui)

    def retranslateUi(self, scui):
        _translate = QtCore.QCoreApplication.translate
        scui.setWindowTitle(_translate("scui", "登陆成功"))
        self.label.setText(_translate("scui", "欢迎，xxx同学"))
        self.pushButton.setText(_translate("scui", "点击查询"))

