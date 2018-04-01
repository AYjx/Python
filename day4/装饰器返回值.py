#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
def outer(func):
    def inner():
        print("before")
        ret = func()
        print("after")
        return ret
    return inner
@outer
def f1():
    print("F1")
    return "原函数f1的返回值"