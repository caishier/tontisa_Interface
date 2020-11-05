#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/29 9:15
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : test_login.py
# @Software: PyCharm
import json
import os
import unittest
from librarys.ddt import data, ddt
from common.read_excel import ReadExcel
from common.logger import logger
from common.config import conf
from common.constant import DATA_DIR
from common.http_request import HTTPRequest2
from common.do_postgresql import ReadPostfresql
from common.text_replace import replace
# 配置文件中读取excel相关数据
file_name = conf.get('excel', 'file_name')



@ddt
class Query(unittest.TestCase):
    wb = ReadExcel(os.path.join(DATA_DIR, file_name), 'query')
    cases = wb.read_data_obj()

    @classmethod
    def setUpClass(cls):
        logger.info('开始自己注册接口的用例，正在准备')
        # 创建一个操作数据库的对象和发请求的对象
        cls.db = ReadPostfresql()
        cls.request = HTTPRequest2()

    @classmethod
    def tearDownClass(cls):
        logger.info('注册接口的用例执行完毕')
        cls.db.close()
        cls.request.close()

    @data(*cases)
    def test_addProduct(self,case):
        #准备数据
        url = conf.get('env', 'url') + case.url
        case.data = replace(case.data)



        # 判断sql语句是否为空
        if case.check_sql:
            case.check_sql = replace(case.check_sql)

        try:
            # 发送请求
            url = conf.get('env', 'url') + case.url
            res = self.request.request(method=case.method, url=url, json=eval(case.data))
            # 比对结果
            logger.info('\n预期结果:{}\n实际结果:{}'.format(case.excepted, res.text))

            self.assertEqual(case.excepted, int(res.json().get('status')))
        except AssertionError as e:
            # 输出日志
            logger.error('\n用例--{}--未通过'.format(case.title))
            logger.error(e)
            # 结果写入文件
            self.wb.write_data(row=case.case_id + 1, column=10, msg='failed')
            raise e
        else:
            logger.info('\n测试用例--{}---已通过'.format(case.title))
            self.wb.write_data(row=case.case_id + 1, column=10, msg='pass')



