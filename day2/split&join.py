#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
'''
username = input("user:")
if username.strip() == "YJX":
    #加上strip()表示移除空白，默认移除空格和换行
    print("Welcome")
    '''

str = "abcdecfghcjkl"
str2 = str.split('c')   #以‘c’为标志分割字符串
str3 = '+'.join(str2)
print(str2)
print(str3)
#print("+".join(str2))   #以‘+’为标志组合字符串