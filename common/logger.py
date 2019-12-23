#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/10 10:38
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : logger.py
# @Software: PyCharm
import os
import logging
from common.config import conf
from common.constant import LOG_DIR



#读取配置文件中相关数据
logger_name = conf.get('logs','logger_name')
level = conf.get('logs','level').upper()
sh_level = conf.get('logs','sh_level').upper()
fh_level = conf.get('logs','fh_level').upper()
log_file  = conf.get('logs','log_file')
#拼接日志文件路径
log_path = os.path.join(LOG_DIR,log_file)


class MyLogging():
    #自定义日之类
    def __new__(cls, *args, **kwargs):
        #创建自己的日志收集器
        my_log = logging.getLogger(logger_name)
        my_log.setLevel(level)
        #创建一个日志输出渠道(控制台)
        l_s = logging.StreamHandler()
        l_s.setLevel(sh_level)
        #创建一个日志输出渠道（文件）
        l_f = logging.FileHandler(log_path,encoding='utf8')
        l_f.setLevel(sh_level)
        #将输出渠道添加到日志收集器中
        my_log.addHandler(l_s)
        my_log.addHandler(l_f)
        #设置日志输出格式
        ft = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        ft = logging.Formatter(ft)
        #设置日志输出格式
        l_s.setFormatter(ft)
        l_f.setFormatter(ft)
        return my_log

logger = MyLogging()



