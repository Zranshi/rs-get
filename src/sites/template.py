# -*- coding:utf-8 -*-
# @Time     : 2021/08/04 16:11
# @Author   : Ranshi
# @File     : template.py
# @Doc      : 处理网站的模版

from bs4 import BeautifulSoup
from src.api.interface import Scrap
from src.api.tool_func import exists_or_create, request
from src.config.path import DATE, ROOT_PATH

# TODO 修改template为自定义文件夹名
GROUP_PATH = f'{ROOT_PATH}/{DATE}/template/'


# TODO [必须完成]修改Template为自定义类名，一般和网站相关，然后需要到__init__.py注册
class ScrapTemplate(Scrap):
    def __init__(self, url: str):
        """构造函数

        Args:
            url (str): url地址
        """

        # TODO [必须完成]handle函数，以设置如何保存数据
        def handle(link: str, **kwargs):
            """保存从scrap函数获得的链接地址的数据的方法

            Args:
                link (str): 链接地址
            """
            ...

        self.soup = BeautifulSoup(request(url).text, 'html.parser')
        dir_path = '/'.join([
            GROUP_PATH,
            self.soup.find('title'),  # TODO 可以自定义从url中获取文件夹名
        ])  # 获取文件夹的绝对路径
        exists_or_create(dir_path)  # 如果不存在则创建文件夹
        Scrap.__init__(
            self,
            url=url,
            handle_link=handle,
            dir_path=dir_path,  # 可以以字典形式传递其他参数，参数可以登录到handle函数的kwargs参数中
        )  # 运行接口的构造函数
        ...

    # TODO [必须完成]从入口链接获取所有待爬取的链接的方法
    def scrap(self) -> str:
        """从self.url和self.soup中获取需要爬取的所有url路径的生成器

        Yields:
            str: 生成的url
        """
        ...
