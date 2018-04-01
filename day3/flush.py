#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
#2、操作文件

f = open('df3','a+',encoding="utf-8")
f.write("\nabs")
f.flush() #强制刷新文件内部缓冲区
input("asdf")
f = open('df3','w')
print(f.readable()) #是否可读
print(f.writable()) #是否可写