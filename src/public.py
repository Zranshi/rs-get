# -*- coding:utf-8 -*-
# @Time     : 2021/7/1 13: 44
# @Author   : Ranshi
# @File     : public.py

import argparse
import os

import aiohttp
import requests

from src.config import HEADERS, PROXYS


def exists_or_create(path: str) -> None:
    """是否存在文件夹，如果不存在则创建文件夹

    Args:
        path (str): 文件夹的路径
    """
    if not os.path.exists(path):
        print(f'save path: {path} is not exists, but I have made it.')
        os.makedirs(path)


def request(url: str) -> requests.models.Response:
    """封装的请求，设置了请求头和代理

  Args:
      url (str): url网址

  Returns:
      requests.models.Response: 响应对象
  """
    res = requests.get(url, headers=HEADERS, proxies=PROXYS)
    return res


def get_parser() -> argparse.Namespace:
    """获取命令行参数

  Returns:
      argparse.ArgumentParser: 命令行参数对象
  """
    parser = argparse.ArgumentParser(
        prog='rs-downImage',
        description='download images',
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
        choices=['th', 'pr', 'co', ''],
        dest='kind',
    )
    return parser.parse_args()


async def fetch_content(url: str):
    """aiohttp异步请求封装

    Args:
        url (str): 请求url

    Returns:
        [type]: 返回的响应对象
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
