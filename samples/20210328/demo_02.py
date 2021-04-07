#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_02.py
# @time: 2021/3/28 9:18 上午

import re

str1 = 'hello123hello'
str2 = '''
hello123hello
hello1hello
'''
# result = re.match('\d+hello',str1) # match 匹配开头
result01 = re.match( '\shello[\d,\D]+o',str2 )
print( result01.group() )

str3 = '''newdream come on!
newdream come good!
'''
# result02 =  re.match( '.+ .+ .+' ,str3)  # (.+?)

# result02 =  re.match( '(.+) (.+) (.+)!' ,str3)  # (.+?)
# print( result02.group(3) )
# print( result02.group(1) )
# print( result02.group(1,3) )

result02 = re.match( '(.+)\sCOme (.+)!\s',str3 ,re.I )
print( result02 )


