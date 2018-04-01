#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
aname = 'yyy'
def show():
    a = 123
    b = 22
    print(locals())
    #所有的局部变量
    print(globals())
    # 所有的全局变量
show()
