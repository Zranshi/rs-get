# -*- coding:utf-8 -*-
# @Time     : 2021/08/04 21:32
# @Author   : Ranshi
# @File     : cli_args.py
# @Doc      : 命令行参数配置
import argparse


def get_parser() -> argparse.Namespace:
    """
    获取设置的命令行参数
    Returns:命令行参数对象

    """
    parser = argparse.ArgumentParser(
        prog="rs-get",
        description="get something !",
    )

    parser.add_argument(
        type=str,
        help="Request entry link.",
        dest="url",
    )
    parser.add_argument(
        "-k",
        type=str,
        default="",
        help="Download ways.",
        choices=["th", "pr", ""],
        dest="kind",
    )
    parser.add_argument(
        "-m",
        type=int,
        default=32,
        help="Maximum concurrent number.",
        dest="max_c",
    )
    parser.add_argument(
        "--app",
        help="Start with application.",
        action="store_true",
    )

    return parser.parse_args()
