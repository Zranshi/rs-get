# -*- coding:utf-8 -*-
# @Time     : 2021/7/1 13: 44
# @Author   : Ranshi
# @File     : public.py
import argparse
import os

import requests

from src.config import HEADERS, PROXYS


def get_parser() -> argparse.Namespace:
    """
    获取命令行参数
    Returns:命令行参数对象

    """
    parser = argparse.ArgumentParser(
        prog='rs-get',
        description='get something !',
    )
    parser.add_argument(
        type=str,
        help='url',
        dest='url',
    )
    parser.add_argument(
        '-k',
        '--kind',
        type=str,
        default='',
        help='kind',
        choices=['th', 'pr', ''],
        dest='kind',
    )
    return parser.parse_args()


def exists_or_create(path: str) -> None:
    """
    是否存在文件夹，如果不存在则创建文件夹
    Args:
        path: 文件夹的路径

    """
    if not os.path.exists(path):
        print(f'Making dir : {path} ...')
        os.makedirs(path)


def request(url: str) -> requests.models.Response:
    """
    封装的请求，设置了请求头和代理
    Args:
        url: url网址

    Returns: 响应对象

    """
    res = requests.get(url, headers=HEADERS, proxies=PROXYS)
    return res
