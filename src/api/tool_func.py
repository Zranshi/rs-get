# -*- coding:utf-8 -*-
# @Time     : 2021/08/04 15:37
# @Author   : Ranshi
# @File     : tool_func.py
# @Doc      : 工具函数
import os
import requests
from src.config.request import HEADERS, PROXYS


def exists_or_create(path: str) -> None:
    """是否存在文件夹，如果不存在则创建文件夹

    Args:
        path: 文件夹的路径

    """
    if not os.path.exists(path):
        print(f'Making dir : {path} ...')
        os.makedirs(path)


def request(url: str) -> requests.models.Response:
    """封装的请求，设置了请求头和代理

    Args:
        url: url网址

    Returns: 响应对象

    """
    res = requests.get(url, headers=HEADERS, proxies=PROXYS)
    return res


def time_log(func, dot_num: int = 2):
    from time import time

    def wrapper(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        stop_time = time()
        print(f'This task took a total of {round(stop_time-start_time, dot_num)} seconds')
        return res

    return wrapper
