# -*- coding:utf-8 -*-
# @Time     : 2021/7/1 13: 44
# @Author   : Ranshi
# @File     : config.py
# @Doc      : 设置文件，包含了请求的头文件以及文件保存根目录
from datetime import date

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0'
}
PROXYS = {'localhost': 7890}
ROOT_PATH = f'/Users/rs/Downloads/{date.today().strftime("%Y.%m.%d")}'
CONST_PATH = '/Users/rs/Downloads/rs-download/'
