#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: email_utlis.py
# @time: 2021/3/21 11:23 上午

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.config_utils import config

class EmailUtils:
    def __init__(self,email_body,email_attch_path=None):
        self.smtp_server = config.SMTP_SERVER
        self.sender = "329999897@qq.com"
        self.password = "wvcsgattkyqqbhah"
        self.receiver = "329999897@qq.com,1992821075@qq.com"
        self.cc = "1004926490@qq.com,2396699745@qq.com"
        self.subject = 'P5P6接口自动化测试报告'
        self.body = email_body
        self.attch_path = email_attch_path

    def email_body(self):
        email_obj = MIMEMultipart()
        email_obj['from'] = self.sender
        email_obj['to'] = self.receiver
        email_obj['Cc'] = self.cc
        email_obj['subject'] = self.subject
        email_obj.attach( MIMEText(self.body,'html','utf-8') )
        if self.attch_path:
            attach_file = MIMEText(open(self.attch_path, 'rb').read(), 'base64', 'utf-8')
            attach_file['Content-type'] = 'application/octet-stream'
            attach_file.add_header('Content-Disposition','attachment',filename=('gbk','',os.path.basename(self.attch_path)) )
            email_obj.attach( attach_file )
        return email_obj

    def send_email(self):
        smtp = smtplib.SMTP()
        smtp.connect( self.smtp_server )
        smtp.login( user=self.sender,password=self.password )
        smtp.sendmail( self.sender, self.receiver.split(",")+self.cc.split(","),self.email_body().as_string())
        smtp.close()

if __name__ == '__main__':
    email_body = '''
    <h1 align="center"> 接口自动化测试报告  </h1>
    <p align="center"> 详情见附件 备注：封装后的 </p>
    '''
    html_file_path = os.path.join(os.path.dirname(__file__), '..', 'html_reports', 'WX_API_TEST_V2.5',
                                  'WX_API_TEST_V2.5.html')
    EmailUtils(email_body,html_file_path).send_email()