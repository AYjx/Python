#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
import random
li = []
for i in range(6):
    r = random.randrange(0,5)
    if r == 0 or r ==3:
        num = random.randrange(0, 10)
        li.append(str(num))
        #将数字转换为字符串并添加到列表li中
    else:
        temp = random.randrange(65,91)
        c = chr(temp)
        #将ASCII码（数字）转换为对应的字母
        li.append(c)
result = "".join(li)  #join函数的元素必须是字符串
print(result)
