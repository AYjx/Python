#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
#全局变量，所有作用域可读
#特殊：列表字典，可修改，不可重新赋值
NAME = "yjx"#定义全局变量大写
def f1():
    age = 18
    global NAME #表示name是全局变量
#修改全局变量时，要在变量前写global
    name = "yj"
    print(age,NAME)
def f2():
    age = 23
    name = "YYY"
#没有添加global，不改变全局变量name
    print(age,NAME)
f1()
f2()
print(NAME)