#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
s1 = {45,668,68}
s2 = {45,586,94}
s3 = {586,55}
s4 = s1.intersection(s2)   #求交集
s1.intersection_update(s2) #将交集返回给s1
set1 = s3.isdisjoint(s2)   #如果没有交集，返回True，否则返回False
set2 = s3.union(s2)   #求并集
set3 = s3.update(s1)   #此时s1={45}
print(s4)
print(s1)
print(set1)
print(set2)
print(s3)
