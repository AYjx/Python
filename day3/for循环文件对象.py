#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
#2、操作文件

f = open('df3','r+',encoding="utf-8")
for line in f:  #循环打印文件的每一行
    print(line)