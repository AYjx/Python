#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
def f1(a1):
    a1.append(666)
li = [11,22,33]
f1(li)
print(li)
#函数传递参数时只传递指针，不复制内容传递
#所以列表li 改变
