#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: log_demo.py
# @time: 2021/3/17 8:33 下午

import logging

# 相当于输出语句，默认输出error级别 ，info是不能输出的
# logging.info('info!!!')
# logging.error('Error!!!')

log_obj = logging.getLogger( 'P5P6' )
log_obj.setLevel(10) # 默认级别 一般配置成最小的
handler1 = logging.StreamHandler()  # 创建handler对象
handler1.setLevel(20)  # 利用handler对象设置日志等级
# 创建了一个日志格式对象
formatter = logging.Formatter("%(asctime)s__%(name)s__%(levelname)s__%(message)s")
#把日志格式对象配置到handler对象
handler1.setFormatter( formatter )

handler2 = logging.FileHandler('./test.log','a',encoding='utf-8')
handler2.setLevel(40)
formatter1 = logging.Formatter("%(asctime)s__liu__%(levelname)s__%(message)s")
handler2.setFormatter(formatter1)

log_obj.addHandler( handler1 )  # 核心 把handler对象设置加载到日志对象
log_obj.addHandler( handler2 )
# formatter -- handler1 -- log_obj
log_obj.debug('debug!!!')
log_obj.info('info!!!')
log_obj.warning('warning!!!')
log_obj.error('error!!!')
log_obj.critical('critical!!!')
