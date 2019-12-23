#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/24 14:51
# @Author : xuancai
# @Email : 444@tontisa.com
# @File : send_email.py
# @Software: PyCharm
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def send_email(filepath):
    """
    :param filepath: 传入报告文件的路径
    :return:
    """
    #第一步 链接到smtp服务器
    s = smtplib.SMTP()
    s.connect(host='smtp.163.com',port=25)

    # 第二步：登录到smtp服务器
    user = "17665209320@163.com"
    pwd = "python3"
    s.login(user=user, password=pwd)

    #构建文件邮件内容
    content = '测试报告附件'
    text_content = MIMEText(content,_charset='utf8')
    #构造附件
    part = MIMEApplication(open(filepath, 'rb').read(), _subtype=True)
    part.add_header('content-disposition', 'attachment', filename='report.html')
    #封装一封邮件
    msg = MIMEMultipart()
    #加入附件和文本内容
    msg.attach(text_content)
    msg.attach(part)
    #添加发件人
    msg['From'] = '17665209320@163.com'
    #添加收件人
    msg['To'] = 'HAHA'
    #添加邮件主题
    msg['Subject'] = Header('测试报告','utf8')
    #发送邮件
    s.sendmail(from_addr='17665209320@163.com',to_addrs='17665209320@163.com',msg=msg.as_string())