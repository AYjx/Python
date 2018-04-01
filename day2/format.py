#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
msg = "Hello,my name is {name},{age} years old!"
msg2 = "man1:{0} ;man2:{1} ;man3:{2}"
msg3 = msg.format(name='yjx',age=23 )      #按名称赋值
msg4 = msg2.format('alex','Tom','Jack')  #按顺序赋值
print(msg3)
print(msg4)
