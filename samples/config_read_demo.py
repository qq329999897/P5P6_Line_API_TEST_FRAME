#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: config_read_demo.py
# @time: 2021/3/14 4:23 下午

import configparser  # 1、导入内置包
import os

config_file_path = os.path.join( os.path.dirname(__file__),'..','conf','config.ini' )

cfg_obj = configparser.ConfigParser()  # 2、创建一个配置文件对象
cfg_obj.read( config_file_path,encoding='utf-8') # 3、配置文件对象加载配置文件
value = cfg_obj.get('path','CASE_PATH') # 4、使用get方法进行取值
print( value )

# 进行二次封装变成更适应框架的代码