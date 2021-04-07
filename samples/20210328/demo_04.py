#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_04.py
# @time: 2021/3/28 9:49 上午

# findall()  查找所有
import re

str1 = 'hello 123 hello'
result_01 = re.search( '\w+',str1 )
result_02 = re.findall( '\w+',str1 )

pattern_01 = re.compile( '\w+' )
result_03 = pattern_01.findall(str1,pos=5,endpos=12)

print( result_01 )
print( result_02 )
print( result_03 )