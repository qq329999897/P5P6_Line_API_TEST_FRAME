#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: log_demo_01.py
# @time: 2021/3/21 8:39 上午


import logging

logger = logging.getLogger( 'work_01' )
logger.setLevel( logging.DEBUG )

console_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s  %(levelno)s  %(levelname)s  %(pathname)s %(filename)s %(funcName)s %(lineno)d  %(thread)d  %(threadName)s  %(process)d  %(message)s")
console_handler.setFormatter( formatter )

logger.addHandler( console_handler )

logger.info('hello,world')
