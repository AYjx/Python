#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
def f1(a1):
    return a1+100
f2 = lambda a1,a2:a1+a2+100
#lambda表达式可代替简单的函数，
#冒号前为参数，后为函数体
ret1 = f1(10)
ret2 = f2(20,25)
print(ret1)
print(ret2)
