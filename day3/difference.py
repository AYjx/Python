#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
s1 = {45,668}
s2 = {45,586}
s3 = {586,55}
s4 = s2.difference(s1)  #返回s2中存在但s1中不存在的元素
s5 = s2.symmetric_difference(s1)   #s2,s1中不相同的取出返回一个新的集合
s2.difference_update(s1)   #将s2中与s1中相同的元素删除
s3.symmetric_difference_update(s2)   #将集合s2和s3中不同的元素返回到s3
print(s4)
print(s5)
print(s2)
print(s3)