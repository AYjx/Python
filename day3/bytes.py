#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
"""s = "课"
n = bytes(s,encoding="utf-8")
m = bytes(s,encoding="gbk")
print(n)
print(m)"""
a = str(bytes("课",encoding="utf-8"),encoding="utf-8")
print(a)