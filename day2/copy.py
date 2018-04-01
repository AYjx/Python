#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
import copy            #第三方库
L= ["2","China",6,["I","am",6,"another"],"list",6,"gf"]
L1 = L.copy()           #不复制深层数据
L2 = copy.copy(L)       #不复制深层数据
L3 = copy.deepcopy(L)   #深度copy，复制深层数据
L[3][2] = "a"
print(L);print(L1);print(L2);print(L3)