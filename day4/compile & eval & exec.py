#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
f = "print('df02')"
r = compile(f,"<string>","exec")
#将字符串编译成python代码
exec(r) #exec执行所有python代码,接收代码或字符串
print(r)
s = "8+6"
ret = eval(s)
ret1 = eval(r)
ret2 = exec(s)
#eval只能执行表达式，执行后有返回值
print(ret)
print(ret1) #eval执行字符串，结果为空
print(ret2) #exec执行表达式，结果为空