#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
#1、打开文件
f = open('df3','a') #
f.write("\n")
#直接传字符串，python自动转换
f.close()
f = open('df3','ab')
f.write(bytes("到啊",encoding="utf-8"))
#不用python做转换，直接传字节
f.close()

