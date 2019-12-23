#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 15:44
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : test_addProduct.py
# @Software: PyCharm
import os
import random
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

def rand_client():
    customer_name = '客户名称'
    for i in range(8):
        i = random.randint(0, 8)
        customer_name += str(i)
    return customer_name


@ddt
class AddProductTestCase(unittest.TestCase):
    wb = ReadExcel(os.path.join(DATA_DIR, file_name), 'addProduct')
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

        if "*customer_name*" in case.data:
            # 未创建的客户名称
            # 方法一：随机生成一个客户名称
            while True:
                customer_name = rand_client()
                # 查询数据库该用户名称是否存在
                count = self.db.find_count("""SELECT * FROM res_partner WHERE name = '{}'""".format(customer_name))
                if count == None:
                    break
            case.data = case.data.replace("*customer_name*", customer_name)

        # 判断sql语句是否为空
        if case.check_sql:
            case.check_sql = replace(case.check_sql)

        try:
            # 发送请求
            url = conf.get('env', 'url') + case.url
            res = self.request.request(method=case.method, url=url, json=eval(case.data))
            # 比对结果
            logger.info('\n预期结果:{}\n实际结果:{}'.format(case.excepted, res.text))

            self.assertEqual(case.excepted, res.text)
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



if __name__ == '__main__':
    def rand_client():
        customer_name = '客户'
        for i in range(8):
            i = random.randint(0, 8)
            customer_name += str(i)
        return customer_name

    db = ReadPostfresql()
    case_data = """ {"id":None,"name":"*customer_name*","nameLang":None,"isManageDataRange":None,"parentId":None,"parentName":None,"parentPath":None,"tags":None,"type":"[1]","fax":None,"partnerType":None,"partnerTypeId":None,"email":None,"website":None,"cityId":None,"cityName":None,"address":None,"createTime":None,"createBy":None,"createByName":None,"partnerUserId":None,"partnerUserName":None,"mobile":None,"remark":None,"ownDeptId":"1397469522389942272","ownDeptName":"同天下","ownUserId":"50","ownUserName":"123","assistUserIds":None,"assistUserNames":None,"currencyCode":"CNY","currencySign":"¥","resPartnerUserList":[],"goodsList":None,"requestResourceId":"282"}
"""
    if "*customer_name*" in case_data:
        # 未创建的客户名称
        # 方法一：随机生成一个客户名称
        while True:
            customer_name = rand_client()
            # 查询数据库该用户名称是否存在
            count = db.find_count("""SELECT * FROM res_partner WHERE name = '{}'""".format(customer_name))
            if count == None:
                break
    case_data = case_data.replace("*customer_name*", customer_name)
    print(case_data)