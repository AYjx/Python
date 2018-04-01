#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
def f1(a):
    if a>2:
        return True
li = [1,2,3,4,5]
ret = filter(f1,li)
print(list(ret))
#filter(函数,可迭代对象-列表、元组),循环第二个参数
#相当于执行下面的函数
# result = [] #空列表用来存放满足条件的元素
# for item in 第二个参数：
#     r = 第一个参数（item）
#     if r:    #若r为真，则返回当前值item
#         result(item)
# return result

ret = filter(lambda a:a>2,li)
#若a>2为真，则lambda表达式返回ture，则filter函数返回当前参数
print(list(ret))