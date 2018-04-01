#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
#str.format()  格式化输出
s = "number {0} is {1}".format(8,'alex')
s1 = "number {0} is {1}".format(*[10,'alex'])
#可以通过字符串来传递，要加上“*”，顺序不能改变
s2 = "I am {name},{age}".format(name='alex',age=18)
#如果{ }里面有字符名，那么赋值时也要指出赋给对象的名称，顺序可以变化
dict = {'name':'alex','age':20}
s3 = "I am {name},{age}".format(**dict)
#也可以通过字典来传递，要加上“**”
print(s)
print(s1)
print(s2)
print(s3)