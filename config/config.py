#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'生产环境配置文件'
__author__ = 'Jiateng Liang'

# 数据库配置
DB_USERNAME = 'root'
DB_PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'blog'
DB_URL_CONNECTION = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + HOST + '/' + DB_NAME
