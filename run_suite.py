#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/9 15:51
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : run_suite.py
# @Software: PyCharm
import os
import time
import unittest
from librarys.HTMLTestRunnerNew import HTMLTestRunner
from common.constant import CASE_DIR,REPORT_DIR
from common.config import conf
from common.send_email import send_email

# 读取测试报告存放的文件名
file_name = conf.get('report','file_name')
# 获取当前时间
file_name = time.strftime("%Y%m%d%H%M%S", time.localtime())+file_name

# 创建一个测试集合
suite = unittest.TestSuite()


# 创建loader对象
loader = unittest.TestLoader()

# 添加测试用例
suite.addTest(loader.discover(CASE_DIR))

filepath = os.path.join(REPORT_DIR,file_name)

# 执行测试用例生成测试报告
with open(filepath, 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='接口测试报告',
        description='测试报告',
        tester='shier')
    runner.run(suite)


# 发送测试报告到邮箱
send_email(filepath)