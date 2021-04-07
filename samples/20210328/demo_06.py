#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_06.py
# @time: 2021/3/28 10:28 上午

#
import re

str1 = '中国$韩国$泰国$英国'
print( str1.split('$') )

str2 = '中国1韩国2泰国3英国'
print( re.split( '\d', str2,maxsplit=2) )  # maxsplit maxsplit=1 分隔一次，默认为 0，不限制次数

str3 = '中国 韩国  泰国       英国    德国'
print( re.split('\s+',str3) )

