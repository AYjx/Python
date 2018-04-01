#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
s1 = {45,668,68}
s2 = {45,586,94}
s3 = {586,55,58,59,34,67,91,61}
s1.discard(45)   #删除指定元素
s2.remove(45)    #删除指定元素
s3.pop()      #随机删除元素
print(s1)
print(s2)
print(s3)