# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setWindowModality(QtCore.Qt.WindowModal)
        Login.resize(418, 313)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Login.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(160, 50, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 151, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.graphicsView = QtWidgets.QGraphicsView(Login)
        self.graphicsView.setGeometry(QtCore.QRect(160, 200, 72, 27))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(90, 250, 81, 28))
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Login)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 250, 81, 28))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(100, 50, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Login)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 150, 151, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(90, 150, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.lineEdit, self.lineEdit_2)
        Login.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Login.setTabOrder(self.lineEdit_3, self.graphicsView)
        Login.setTabOrder(self.graphicsView, self.pushButton)
        Login.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "成绩查询"))
        self.pushButton.setText(_translate("Login", "登陆"))
        self.pushButton_2.setText(_translate("Login", "取消"))
        self.label.setText(_translate("Login", "学号："))
        self.label_2.setText(_translate("Login", "密码："))
        self.label_3.setText(_translate("Login", "验证码："))

