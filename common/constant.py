#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/9 15:56
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : constant.py
# @Software: PyCharm
"""
封装动态获取常量
"""
import os
#获取项目目录的根路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#获取配置文件存放目录
CONF_DIR = os.path.join(BASE_DIR,'conf')

#日志保存的文件目录路径
LOG_DIR = os.path.join(BASE_DIR,'logs')

#excel数据存放目录路径
DATA_DIR = os.path.join(BASE_DIR,'data')

#测试用例存放目录路径
CASE_DIR = os.path.join(BASE_DIR,'testcases')

#测试报告存放目录路径
REPORT_DIR = os.path.join(BASE_DIR,'reports')

