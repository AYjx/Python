#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
#1、打开文件
f = open('df3','r+',encoding="utf-8")
#从指针的位置开始读写
f.seek(3)
data = f.read(1) #读取一个字符
print(data)
print(f.tell()) #获取当前指针的位置（按字节）
#f.seek() #将指针调到指定的位置（按字节的个数）
f.write("理解") #从当前指针位置向后覆盖
f.close()