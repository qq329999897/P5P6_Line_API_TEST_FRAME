#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: email_demo_01.py
# @time: 2021/3/21 10:45 上午

import smtplib
from email.mime.text import MIMEText

email_body = '''
<h1 align="center"> 接口自动化测试报告  </h1>
<p align="center"> 详情见附件 </p>
'''

email_obj = MIMEText(email_body,'html','utf-8')
email_obj['from'] = '329999897@qq.com' # 发件人
email_obj['to'] = 'hello@qq.com' # 收件人
email_obj['Cc'] = '1004926490@qq.com,hello@qq.com' # 抄送人
email_obj['subject'] = 'P5P6接口自动化测试报告'

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
# 邮箱授权码：
smtp.login(user='329999897@qq.com',password='wvcsgattkyqqbhah')
# smtp.sendmail("329999897@qq.com",'329999897@qq.com',email_obj.as_string())
smtp.sendmail("329999897@qq.com",['329999897@qq.com','1004926490@qq.com'],email_obj.as_string())
smtp.close()



