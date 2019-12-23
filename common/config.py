#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/9 15:54
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : config.py
# @Software: PyCharm
import os
import configparser
from common.constant import CONF_DIR

class ReadConfig(configparser.ConfigParser):
    def __init__(self):
        #实例化对象
        super().__init__()
        #加载文件
        #创建加载配置文件的对象
        r = configparser.ConfigParser()
        #读取开关文件
        r.read(os.path.join(CONF_DIR,'env.ini'),encoding='utf8')
        switch = r.get('env','switch')
        #判断开关的值，选择加载环境的配置
        if switch == '1':
            self.read(os.path.join(CONF_DIR,'config2.ini'),encoding='utf8')
        else:
            self.read(os.path.join(CONF_DIR,'config1.ini'),encoding='utf8')
conf = ReadConfig()