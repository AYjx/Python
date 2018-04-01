#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
L= ["2","China",6,"I","am",6,"another","list",6,"gf"]
L2 = ["hh","kk","ss"]
L2.insert(0,"YYY")      #将数据“YYY”插入到L的0号位置
print(L2)
L2.append("666")        #将数据添加到L的末尾
print(L2)
L2.extend("666")        #“666”被分开添加到列表L末尾
print(L2)
L.extend(L2)             #将列表L2添加到列表L的末尾
print(L)
L.remove(6)              #删除列表中的第一个常数6，不是字符“6”
print(L)