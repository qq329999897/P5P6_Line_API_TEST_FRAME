#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_04.py
# @time: 2021/3/28 9:49 上午

# re.finditer  查找所有 并返回迭代器 迭代器中都是match对象
import re

str1 = 'hello 123 hello'

pattern_01 = re.compile( '\w+' )
result_03 = pattern_01.finditer(str1,pos=5,endpos=12)
print( type(result_03) )  #

for r in result_03:
    print( r.group() )
