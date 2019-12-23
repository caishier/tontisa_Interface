#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/17 15:32
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : text_replace.py
# @Software: PyCharm

import re
from common.config import conf

class ConText():
    # 用来存储临时变量
    loan_id = None


def replace(data):
    """
    用例参数替换
    :param data:用例参数
    :return:
    """
    p = r"#(.+?)#"
    # 判断该用例参数中是否有需要替换的
    while re.search(p, data):
        # 去配置文件中获取要替换的数据
        key = re.search(p, data).group(1)
        try:
            # 去配置文件中查找，如果不存在的话，应该就是临时生成的数据
            value = conf.get('test_data', key)
        except:
            value = getattr(ConText, key)
        # 替换
        data = re.sub(p, value, data, count=1)
    return data