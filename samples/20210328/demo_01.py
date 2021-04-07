#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_01.py
# @time: 2021/3/28 8:57 上午

# 正则表达式基础

import re

str1 = 'newdream'
str2 = '''
hello123hello
hello123
hello12
12hello
hello12ho
'''

# 方式一：
pattern_01 = re.compile( 'n\w+m' )
result_01 = re.match( pattern_01 , str1 )
print( result_01.group() )

pattern_02 = re.compile('hello\d+h')
result_02 = re.findall( pattern_02 , str2 )
print( result_02 )

# 方式二：
result_03 = re.match( 'n\w+m' ,str1 )
print( result_03.group() )

# 方式三：
result_04 = pattern_01.match( str1 )
print( result_04.group() )