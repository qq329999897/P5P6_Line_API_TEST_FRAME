#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_08.py
# @time: 2021/3/28 10:59 上午

import re

str1 = '''newdream come on!!
google come on!!'''
value = re.subn('(\w+) (\w+) (\w+)',r'\2 \3 \1',str1)
print( type(value) )
print( value )