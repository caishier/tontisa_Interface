#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/20 14:40
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : test.py
# @Software: PyCharm

##第一次去掉ab子串后拼接还是会有ab子串：abcdbaac
##第二次再次去掉ab子串后结果为：cdbaac
str = 'aabbcdbaaabc'
a = str.split('ab')
print(a)
b = ''.join(a)
print(b)
c = b.split('ab')
d = ''.join(c)
print(d)