#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/9 16:17
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : do_postgresql.py
# @Software: PyCharm

import psycopg2
from common.config import conf


class ReadPostfresql(object):
    # 连接数据库
    def __init__(self):
        self.con = psycopg2.connect(
            host = conf.get('sql', 'host'),
            port = conf.getint('sql', 'port'),
            user= conf.get('sql', 'user'),
            password = conf.get('sql', 'password'),
            database = conf.get('sql', 'database'),

        )
        #创建游标
        self.cur = self.con.cursor()

    def find_one(self, sql):
            """
            返回找到的第一条数据
            :param sql:
            :return:
            """
            self.cur.execute(sql)
            self.con.commit()
            return self.cur.fetchone()

    def find_all(self, sql):
        """
        返回找到的所有数据
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.fetchall()

    def find_count(self, sql):
        """
        # 查找存在的数据条数
        :return:
        """
        count = self.cur.execute(sql)
        self.con.commit()
        return count

    def close(self):
        """断开连接"""
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    db = ReadPostfresql()
    sql = "select * from sys_user where mobile = '17531022770'"
    rs = db.find_one(sql)
    print(rs)