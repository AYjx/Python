#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
l1 = ["y",1,2,3]
l2 = ["j",4,5,6]
l3 = ["x",7,8,9,0]
ret = zip(l1,l2,l3)
#zip将列表中的元素一一对应组合，多余的舍弃
temp = list(ret)[0]
ret1 = ' '.join(temp)
print(ret1)