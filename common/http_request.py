#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/9 18:00
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : http_request.py
# @Software: PyCharm
import json

import requests
from common.logger import logger



class HTTPRequest(object):
    """
    发送请求不记录cookie
    """
    def request(self, method, url,
                params=None, data=None,
                headers=None, cookies=None, json=None):
        #判断请求的方法
        method = method.lower()
        if method == 'POST':
            #判断是够用json传递参数
            if json:
                logger.info('正在发送请求，请求地址：{}，请求参数：{}'.format(url, json))
                return requests.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                logger.info('正在发送请求，请求地址：{}，请求参数：{}'.format(url, data))
                return requests.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == 'get':
            logger.info('正在发送请求，请求地址：{}，请求参数：{}'.format(url, params))
            return requests.get(url=url, params=params, headers=headers, cookies=cookies)



class HTTPRequest2(object):
    """记录cookies信息,给下一次请求用 """

    def __init__(self):
        # 创建一个session对象
        self.session = requests.sessions.Session()

    def request(self, method, url,
                 data=None,headers=None,
                cookies=None, json=None):
        # 判断请求的方法

        method = method.lower()
        if method == 'post':
            # 判断是否使用json来传参（适用于项目中接口参数有使用json传参的）
            if json:
                logger.info('正在发送请求，请求地址：{}，请求参数：{}'.format(url, json))
                return self.session.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                logger.info('正在发送请求，请求地址：{}，请求参数：{}'.format(url, data))
                return self.session.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == 'get':
            logger.info('正在发送请求，请求地址：{}，请求参数：{}'.format(url, data))
            return self.session.get(url=url, params=data, headers=headers, cookies=cookies)

    def close(self):
        self.session.close()

# class GetData(object):
#     def login(self):
#         url = "http://xqtest.op110.com.cn/tontisa-xq-shiro/ajaxLogin"
#         data = {
#             "username": "admin",
#             "password": "12345678"
#         }
#         response = requests.post(url=url, json=json.dumps(data))
#         return response.cookies
#
#
#
# if __name__ == '__main__':
#     url = "http://xqtest.op110.com.cn/tontisa-xq-shiro/ajaxLogin"
#     data = {
#         "username":"admin",
#         "password":"12345678"
#     }
#     response = requests.post(url=url, json=data)
#     print(response.text)
#     print(response.status_code)
#     print(response.cookies)

