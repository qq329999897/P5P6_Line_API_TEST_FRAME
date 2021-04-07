#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_03.py
# @time: 2021/3/28 9:42 上午

# search 函数  全字符串查找  找到第一个就停止
import re

str1 = 'nEwDreamEaaaa'
# pattern_01 = re.compile( 'e\w' ,re.IGNORECASE )
# result_01 = re.search( pattern_01 , str1   )
result_01 = re.search( 'e\w' , str1 ,re.I   )
print( result_01.group() )
