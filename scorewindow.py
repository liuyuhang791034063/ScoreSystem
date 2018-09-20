# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       scorewindow
   Description:
   Author:           God
   date：            2018/7/30
-------------------------------------------------
   Change Activity:  2018/7/30
-------------------------------------------------
"""
import sys
import time

__author__ = 'God'

from PyQt5.QtWidgets import *
from score import Ui_Form
import education_system
from scorestatistics_ui import Ui_Score

all_date = dict()


class ScoreWindow(QMainWindow, Ui_Form):
    def __init__(self, url, xh, cookie):
        super(ScoreWindow, self).__init__()
        self.setupUi(self)
        self.xh = xh
        self.url = url
        self.cookie = cookie
        all_date = education_system.get_box_date(cookie, url, xh)
        # 添加学年
        for i in all_date.get('top_box').get('xn'):
            if i == '':
                continue
            self.comboBox.addItem(i)
        # 添加学期
        for i in all_date.get('top_box').get('xq'):
            if i == '':
                continue
            self.comboBox_2.addItem(i)
        # 添加课程性质
        self.comboBox_3.addItem("全部课程")
        for i in all_date.get('top_box').get('kcxz'):
            if i == '':
                continue
            self.comboBox_3.addItem(i)
        self.pushButton.clicked.connect(lambda: self.getdate(self.pushButton.text(), all_date))
        self.pushButton_4.clicked.connect(lambda: self.getdate(self.pushButton_4.text(), all_date))
        self.pushButton_5.clicked.connect(lambda: self.getdate(self.pushButton_5.text(), all_date))
        self.pushButton_6.clicked.connect(lambda: self.getdate(self.pushButton_6.text(), all_date))
        self.pushButton_8.clicked.connect(lambda: self.getdate(self.pushButton_8.text(), all_date))
        self.pushButton_9.clicked.connect(lambda: self.getscocestatistics(self.pushButton_9.text(), all_date))
        all_date["date_url"] = url

    # 获取成绩信息
    def getdate(self, str1, all_date_dict):
        date_dict = dict()
        date_dict["xn"] = self.comboBox.currentText()
        date_dict["xq"] = self.comboBox_2.currentText()
        date_dict["kcxz"] = all_date_dict.get("top_box").get("kcxz").get(self.comboBox_3.currentText())
        date_dict["btn_date"] = all_date_dict.get("btn_date").get(str1)
        date_dict["vie"] = all_date_dict.get("re_header").get("__VIEWSTATE")
        date_dict["url"] = self.url
        date_dict["cookies"] = all_date_dict.get("cookies")
        search_date = education_system.search_date(date_dict)
        all_score = search_date.get("score")
        header = all_score.pop(0)
        columns = len(header)
        rows = all_score.__len__()
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(columns)
        self.tableWidget.setHorizontalHeaderLabels(header)
        for i in range(rows):
            for j in range(len(all_score[i])):
                newitem = QTableWidgetItem(all_score[i][j])
                self.tableWidget.setItem(i, j, newitem)

    # 获取成绩统计
    def getscocestatistics(self, button_str, all_date_dict):
        date_dict = dict()
        date_dict["xn"] = self.comboBox.currentText()
        date_dict["xq"] = self.comboBox_2.currentText()
        date_dict["kcxz"] = all_date_dict.get("top_box").get("kcxz").get(self.comboBox_3.currentText())
        date_dict["btn_date"] = all_date_dict.get("btn_date").get(button_str)
        date_dict["vie"] = all_date_dict.get("re_header").get("__VIEWSTATE")
        date_dict["url"] = self.url
        date_dict["cookies"] = all_date_dict.get("cookies")
        search_date = education_system.search_score_statistics(date_dict)
        # 生成成绩统计对象
        self.sd = ScoreStatistics(search_date.get('xftj'), search_date.get('score'))
        # 对象显示
        self.sd.show()


class ScoreStatistics(QWidget, Ui_Score):
    def __init__(self, xftj, score):
        """
        :param xftj: str
        :param score: List
        """
        super(ScoreStatistics, self).__init__()
        self.setupUi(self)
        self.label.setText(xftj)
        # 设置表格头
        header = score.pop(0)
        # 设置表格列长
        columns = len(header)
        # 设置表格行长
        rows = score.__len__()
        self.tableWidget.setColumnCount(columns)
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setHorizontalHeaderLabels(header)
        for i in range(rows):
            for j in range(len(score[i])):
                newitem = QTableWidgetItem(score[i][j])
                self.tableWidget.setItem(i, j, newitem)




