#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
def f1(*args):
#在参数前加“*”号，则在调用函数时添加的参数放入元组
    print(args,type(args))
f1(11)
li = [5,6,7,'d','e']
f1(li,'Arm')   #整个列表作为元组的一个元素
f1(*li,'Arm')  #列表中的元素分别放入为元组中