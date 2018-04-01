#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
A = []
for i in range(0, 3):
    tmp = []
    for j in range(0, 3):
        tmp.append(j)
    A.append(tmp)
A = A.dot(A)
print(A)