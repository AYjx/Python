#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
def f2(**args1):
# 在参数前加“**”，则在调用函数时添加的参数默认放入字典
    print(args1, type(args1))
f2(li = 123,li2 = 'abc') #赋一个key配一个value
dict = {'k1':'v1','k2':'v2'}
f2(**dict)  #将dict中的元素分别放入字典中