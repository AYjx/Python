#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
def outer(func):
    def inner():
        print("before")
        func()    #执行原来的f1函数
        print("after")
    return inner
#返回inner，函数f1被重新赋值成装饰器的内置函数
@outer #此处不执行outer函数内部的inner函数，只返回inner给函数f1
def f1():  #程序运行到函数f1时执行inner函数
    print("F1")
# @outer
# def f2():
#     print("F2")