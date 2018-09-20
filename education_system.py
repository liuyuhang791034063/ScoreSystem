# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       education_system
   Description:      教务系统爬虫
   Author:           God
   date：            2018/7/27
-------------------------------------------------
   Change Activity:  2018/7/27
-------------------------------------------------
"""
__author__ = 'God'

from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import quote
# from PIL import Image

header1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
}

login_data = {
    'Textbox1': '',
    'lbLanguage': '',
    'hidsc': '',
    'hidPdrs': '',
    'Button1': '',
    'RadioButtonList1': '%D1%A7%C9%FA',
}

login_url = 'http://222.24.62.120/default2.aspx'  # 修改本校教务系统登陆url
code_url = 'http://222.24.62.120/CheckCode.aspx'  # 修改本校教务系统验证码url
referer_url = "http://222.24.62.120/xs_main.aspx?xh="  # 根据本校教务系统修改格式


def get_box_date(cookie, url, xh):
    header = header1
    header['Referer'] = referer_url + str(xh)
    html = requests.get(url, headers=header, cookies=cookie)
    all_date = dict()
    all_date['cookies'] = cookie
    soup = BeautifulSoup(html.text, "html.parser")
    re_header = dict()
    re_header['__EVENTTARGET'] = soup.find("input", attrs={"name": "__EVENTTARGET"}).attrs.get("value")
    re_header['__EVENTARGUMENT'] = soup.find("input", attrs={"name": "__EVENTARGUMENT"}).attrs.get("value")
    re_header['__VIEWSTATE'] = soup.find("input", attrs={"name": "__VIEWSTATE"}).attrs.get("value")
    all_date['re_header'] = re_header
    top_box = dict()
    top_box['xn'] = {x.text: x.attrs.get("value") for x in
                     soup.find('select', attrs={"name": "ddlXN"}).find_all("option")}
    top_box['xq'] = {x.text: x.attrs.get("value") for x in
                     soup.find('select', attrs={"name": "ddlXQ"}).find_all("option")}
    top_box['kcxz'] = {x.text: x.attrs.get("value") for x in
                       soup.find('select', attrs={"name": "ddl_kcxz"}).find_all("option")}
    top_box['kcxz']["全部课程"] = ''
    all_date['top_box'] = top_box
    all_date['btn_date'] = {x.attrs.get("value"): [quote(x.attrs.get("value"), encoding="gbk"), x.attrs.get("name")] for
                            x in soup.find_all('p', class_="search_con")[1].find_all("input")[:-1]}
    return all_date


def get_code():
    s = requests.session()
    r = s.get(code_url, headers=header1)
    with open("code.png", "wb+") as e:
        e.write(r.content)
    return s


def login(xh, mm, code, s):
    login_data['txtUserName'] = xh
    login_data['TextBox2'] = mm
    login_data['txtSecretCode'] = code
    r = s.get(login_url)
    soup = BeautifulSoup(r.text, "html.parser")
    value = soup.find_all(attrs={"name": "__VIEWSTATE"})
    login_data['__VIEWSTATE'] = value[0].attrs['value']
    index_html = s.post(url=login_url, headers=header1, data=login_data)
    if re.findall(re.compile('<title>(.+?)</title>'), index_html.text)[0] == "正方教务管理系统":
        soup = BeautifulSoup(index_html.text, "html.parser")
        name = soup.find("span", id="xhxm").text.split('同')[0]
        return True, s.cookies, name
    else:
        return False, s.cookies, ''


def search_date(date_dict):
    MAX_COLUMNS = 15
    score_data = {
        '__VIEWSTATE': date_dict.get("vie"),
        date_dict.get("btn_date")[1]: date_dict.get("btn_date")[0],
        'ddl_kcxz': date_dict.get("kcxz"),
        'ddlXN': date_dict.get("xn"),
        'ddlXQ': date_dict.get("xq"),
    }
    header = header1
    header["Referer"] = date_dict.get("url")
    date_url = date_dict.get("url")
    cookie = date_dict.get("cookies")
    try:
        score_html = requests.post(url=date_url, headers=header, data=score_data, cookies=cookie)
    except AttributeError:
        print(print('获取信息失败'))
        return
    soup = BeautifulSoup(score_html.text, 'html.parser')
    date = {}
    all_dates = soup.find('table', id='Table1')
    table_name = all_dates.find('span', id='lbl_bt').text
    date['table_name'] = table_name
    student_date = {}
    lbl_xh = all_dates.find('span', id='lbl_xh').text.split("：")[1]
    lbl_xm = all_dates.find('span', id='lbl_xm').text.split("：")[1]
    lbl_xy = all_dates.find('span', id='lbl_xy').text.split("：")[1]
    lbl_zymc = all_dates.find('span', id='lbl_zymc').text
    lbl_xzb = all_dates.find('span', id='lbl_xzb').text
    student_date['stu_xh'] = lbl_xh
    student_date['stu_xm'] = lbl_xm
    student_date['stu_xy'] = lbl_xy
    student_date['stu_zymc'] = lbl_zymc
    student_date['stu_xzb'] = lbl_xzb
    date['student'] = student_date
    all_dates = soup.find('table', id="Datagrid1")
    if all_dates is None:
        MAX_COLUMNS = 6
        all_dates = soup.find('table', id="Datagrid3")
    nums = re.findall(re.compile('<td>(.*?)</td>{1,}', re.S), str(all_dates))
    date['score'] = []
    note = 0
    list = []
    for i in nums:
        note += 1
        i = str(i)
        if "</a>" in i:
            i = re.findall(re.compile('<a .*?>(.*?)</a>'), i)[0]
        list.append(i)
        if note == MAX_COLUMNS:
            note = 0
            date['score'].append(list)
            list = []
    # 旧方法
    # trs = all_dates.find_all('tr')
    # date['score'] = []
    # for i in range(1, len(trs)):
    #     tr = trs[i]
    #     list = []
    #     for i in tr.contents:
    #         if i == '\n':
    #             continue
    #         list.append(re.findall(re.compile('<td>(.*?)</td>'), str(i))[0])
    #     date['score'].append(list)
    return date


def search_score_statistics(date_dict):
    score_data = {
        '__VIEWSTATE': date_dict.get("vie"),
        date_dict.get("btn_date")[1]: date_dict.get("btn_date")[0],
        'ddl_kcxz': date_dict.get("kcxz"),
        'ddlXN': date_dict.get("xn"),
        'ddlXQ': date_dict.get("xq"),
    }
    header = header1
    header["Referer"] = date_dict.get("url")
    date_url = date_dict.get('url')
    cookie = date_dict.get("cookies")
    try:
        score_html = requests.post(url=date_url, headers=header, data=score_data, cookies=cookie)
    except AttributeError:
        print(print('获取信息失败'))
        return
    soup = BeautifulSoup(score_html.text, 'html.parser')
    date = dict()
    date["xftj"] = soup.find('span', id='xftj').text
    date['score'] = list()
    score_date = soup.find('table', id='Datagrid2').find_all('tr')
    for i in score_date:
        date_list = [j.contents[0] for j in i.contents[1:6]]
        date['score'].append(date_list)
    return date
