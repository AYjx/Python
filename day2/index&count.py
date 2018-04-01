#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
L= ["2","China",6,"I","am",6,"another","list",6,"gf"]
print(L.count(6))           #L.count()--计数
print(L.index(6))           #L.index()--检索元素位置
for i in range(L.count(6)): #for循环，逐一修改
    ele_index = L.index(6)
    print(ele_index)        #显示列表元素6的位置
    L[ele_index] = 666      #修改列表元素
print(L)