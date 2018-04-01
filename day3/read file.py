#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
#1、打开文件
# f = open('name','r') #只读文件
#f = open('name','w') #只写，先清空原文件
#f = open('name','x')
# #文件存在，则报错；文件不存在，则创建文件并只写入内容
#f = open('name','a') #追加内容
f = open('df3','r',encoding="utf-8")
  #不加“b”读取到的文件内容为字符串类型
data = f.read()
print(data,type(data))
f = open('df3','rb') #加“b”读取到的文件内容为字节类型
data1 = f.read()
print(data1,type(data1))
