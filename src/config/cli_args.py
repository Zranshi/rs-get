# -*- coding:utf-8 -*-
# @Time     : 2021/08/04 21:32
# @Author   : Ranshi
# @File     : cli_args.py
# @Doc      : 命令行参数配置
import argparse


def get_parser() -> argparse.Namespace:
    """获取命令行参数

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
