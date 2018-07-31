# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       main
   Description:
   Author:           God
   date：            2018/7/27
-------------------------------------------------
   Change Activity:  2018/7/27
-------------------------------------------------
"""
__author__ = 'God'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
