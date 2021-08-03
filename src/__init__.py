# -*- coding:utf-8 -*-
# @Time     : 2021/7/1 13: 43
# @Author   : Ranshi
# @File     : __init__.py
from src.public import get_parser
from src.sites import SITES_MAP


def site_handler(url: str, kind: str = '') -> bool:
    """
    为不同的网站非配不同的子类
    Args:
        url: url地址
        kind: 下载的方式，单线程/多线程/多进程

    Returns: 是否是可以下载

    """
    site = url.split('/')[2]
    if site in SITES_MAP:
        spider = SITES_MAP[site](url=url)
        if not spider.handle(kind=kind):
            return False
    else:
        return False
    return True


def run() -> None:
    args = get_parser()
    if not site_handler(args.url, args.kind):
        print('sorry, this website is not supported this moment.')
