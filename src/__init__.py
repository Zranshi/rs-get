# -*- coding:utf-8 -*-
# @Time     : 2021/7/1 13: 43
# @Author   : Ranshi
# @File     : __init__.py
from src.public import get_parser
from src.sites import SITES_MAP


def site_handler(url: str, kind: str = '') -> bool:
  site = url.split('/')[2]
  if site in SITES_MAP:
    spider = SITES_MAP[site](url=url)
    if not spider.handle(kind=kind):
      return False
  else:
    return False
  return True


def run():
  args = get_parser()
  if not site_handler(args.url, args.kind):
    print('sorry, this website is not supported this moment.')
