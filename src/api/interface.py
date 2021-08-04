# -*- coding:utf-8 -*-
# @Time     : 2021/08/04 15:39
# @Author   : Ranshi
# @File     : interface.py
# @Doc      : 接口类

from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from typing import Callable, Iterable, List

from alive_progress import alive_bar


class Scrap:
    def __init__(self, url: str, handle_link: Callable, **link_kwargs: dict):
        """初始化一个爬取对象

        Args:
            url: 爬取的url地址
            handle_link: 处理函数
            **link_kwargs: 处理函数的参数
        """
        self.url = url
        self.handle_link = handle_link
        self.link_kwargs = link_kwargs

    def handle(self, kind: str, _max: int = 32) -> bool:
        """入口函数，根据命令行参数选择下载方式

        Args:
            kind: 下载方式
            _max: 最大线程/进程数. Defaults to 32.

        Returns: 输入是否合法

        """
        print('links collecting...')
        links = list(self.scrap())
        with alive_bar(len(links), theme='ascii', title='downloading...') as bar:
            if kind == '':
                self.download(links, bar)
            elif kind[:2] == 'th':
                self.download_th(links, bar, _max)
            elif kind[:2] == 'pr':
                self.download_pr(links, bar, _max)
            else:
                return False
        return True

    def download(self, links: Iterable, bar: Callable):
        """使用单线程下载，速度较慢

        Args:
            links: 链接的列表
            bar: 进度条生成器

        """
        for link in links:
            self.handle_link(link=link, **self.link_kwargs)
            bar()

    def download_th(self, links: Iterable, bar: Callable, _max: int = 32):
        """使用多进程进行下载

        Args:
            links: 链接的列表
            bar: 进度条对象
            _max: 线程池大小. Defaults to 32.

        """
        with ThreadPoolExecutor(max_workers=_max) as pool:
            tasks = []
            for link in links:
                tasks.append(
                    pool.submit(
                        self.handle_link,
                        link=link,
                        **self.link_kwargs,
                    ))
            for task in tasks:
                task.result()
                bar()

    def download_pr(self, links: Iterable, bar: Callable, _max: int = 32):
        """使用多进程进行下载

        Args:
            links: 链接的列表
            bar: 进度条对象
            _max: 进程池大小. Defaults to 32.

        """
        tasks = []
        with Pool(processes=_max) as pool:
            for link in links:
                tasks.append(
                    pool.apply_async(
                        func=self.handle_link,
                        args=(link, ),
                        kwds=self.link_kwargs,
                    ))
            for task in tasks:
                task.get()
                bar()

    @classmethod
    def scrap(cls) -> List[str]:
        """从主页面中获取所有需要的资源，并返回所有需要处理的links

        Returns: 返回链接列表

        """
        return []