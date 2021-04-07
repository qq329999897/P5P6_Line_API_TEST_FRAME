#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_07.py
# @time: 2021/3/28 10:36 上午

import re

str1 = '135  7766  8899 , 湖南号码'
str1 = str1.replace(' ','')
print(str1)

str1 = '135  7766 8899 , 湖南号码'
result_01 = re.sub('\d\s+\d','',str1)  #  1376899 , 湖南号码
print( result_01 )
result_02 = re.sub('(\d+)\s+(\d+) (\d+)',r'\1\3\2',str1) # \1 \2 表示()的分组
print( result_02 )
result_03 = re.sub( '\s,.*$','',str1 )
print( result_03 )

# result_02 = re.sub('(\d\s+\d)','',str1)
# print( result_02 )