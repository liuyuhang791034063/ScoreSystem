# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       mainwindow
   Description:
   Author:           God
   date：            2018/7/28
-------------------------------------------------
   Change Activity:  2018/7/28
-------------------------------------------------
"""
__author__ = 'God'

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from urllib.parse import quote

from login_ui import Ui_Login
from aflogin import Ui_afui
from sclogin import Ui_scui
from scorewindow import scorewindow
import education_system


class MainWindow(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.lineEdit_3.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.session = education_system.get_code()
        # 对接登陆
        self.pushButton.clicked.connect(self.getdate)
        # 取消
        self.pushButton_2.clicked.connect(self.close)
        # 放置二维码
        code = QGraphicsPixmapItem(QPixmap("code.png"))
        scence = QGraphicsScene()
        scence.addItem(code)
        self.graphicsView.setScene(scence)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏侧边栏
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏下边栏

    def getdate(self):
        self.xh = self.lineEdit.text()
        mm = self.lineEdit_2.text()
        # self.xh = "04161086"
        # mm = "lyh791034063"
        code = self.lineEdit_3.text()
        status, cookie, name = education_system.login(self.xh, mm, code, self.session)
        self.date_url = "http://222.24.62.120/xscjcx.aspx?xh=" +\
                        str(self.xh) +\
                        "&xm="+quote(name, encoding="gbk") +\
                        "&gnmkdm=N121605"

        if status == True:
            # 返回成功界面
            # education_system.get_box_date(cookie, self.date_url, self.xh)
            self.sc = AfterLoginSc(name, self.date_url, self.xh, cookie)
            self.close()
            self.sc.show()
        else:
            # 返回失败界面
            self.af = AfterLoginFa()
            self.hide()
            self.af.show()

    # esc退出
    def keyPressEvent(self, e):
        e = QKeyEvent(e)
        if e.key()+1 == Qt.Key_Enter:
            self.pushButton.click()
        if e.key() == Qt.Key_Escape:
            self.close()


class AfterLoginFa(QMainWindow, Ui_afui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.new)
        self.pushButton_2.clicked.connect(self.close)

    def new(self):
        self.new = MainWindow()
        self.close()
        self.new.show()

    def keyPressEvent(self, event):
        if event.key()+1 == Qt.Key_Enter:
            self.pushButton.click()
        if event.key() == Qt.Key_Escape:
            self.close()


class AfterLoginSc(QMainWindow, Ui_scui):
    def __init__(self, name, url, xh, cookie):
        super(AfterLoginSc, self).__init__()
        self.setupUi(self)
        self.cookie = cookie
        self.dateurl = url
        self.xh = xh
        self.label.setText("欢迎，%s同学" % name)
        self.pushButton.clicked.connect(self.inquire)

    def inquire(self):
        self.hide()
        self.sc = scorewindow(self.dateurl, self.xh, self.cookie)
        self.sc.show()

    def keyPressEvent(self, event):
        if event.key()+1 == Qt.Key_Enter:
            self.pushButton.click()

