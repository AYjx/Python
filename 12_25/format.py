#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
from math import pi
msg = 'Hello,%s %s !'
msg1 = ('my','world')
msg2 = msg % msg1
'''格式化字符串%的右侧放希望被格
式化的值,左侧放格式化字符串'''
print(msg2)
msg3 = 'pi with three decimals:%.4f'
msg4 = msg3 % pi
print(msg4)