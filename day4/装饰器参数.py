#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
def outer(func):
    def inner(*args,**kargs):
        print("before")
        ret = func(*args,**kargs)
        print("after")
        return ret
    return inner
@outer
def f1(arg1,arg2):#f1有几个参数，装饰器就要几个参数
    print(arg1,arg2)
    return "?"