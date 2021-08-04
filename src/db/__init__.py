# -*- coding:utf-8 -*-
# @Time     : 2021/08/04 15:36
# @Author   : Ranshi
# @File     : __init__.py
# @Doc      : 文件夹存放数据库相关的代码

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.db import Db


def get_db_session():
    return sessionmaker(bind=create_engine(
        f'mysql+pymysql://{Db.user}:{Db.pwd}@{Db.host}:{Db.port}/{Db.db_name}'))()
