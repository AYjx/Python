#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
li = [1,2,3,7,8,9]
def f1(a):
    return a+10
result = map(f1,li)
print(list(result))

result = map(lambda a:a+100,li)
print(list(result))