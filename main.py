# -*- coding:utf-8 -*-
# @Time     : 2021/08/04 21:30
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 程序运行入口
from src.config.cli_args import get_parser
from src.api.tool_func import time_log
from src.sites import SITES_MAP


@time_log
def site_handler(url: str, kind: str = '') -> bool:
    """为不同的网站非配不同的子类

    Args:
        url: url地址
        kind: 下载的方式

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


if __name__ == '__main__':
    args = get_parser()
    if not site_handler(url=args.url, kind=args.kind):
        print('sorry, this website is not supported this moment.')