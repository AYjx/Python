#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
#2、操作文件

f = open('df3','r+',encoding="utf-8")
f.seek(18)
f.truncate() #从指针的位置截断数据
f.close()