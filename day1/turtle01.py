# -*- coding:utf-8 -*-
# Author：YJX
from turtle import *
reset()
speed('fast')
IN_TIMES = 40
TIMES = 20
for i in range(TIMES):
    right(360/TIMES)
    forward(200/TIMES)  #这一步是做什么用的？
    for j in range(IN_TIMES):
        right(360/IN_TIMES)
        forward (400/IN_TIMES)
write(" Click me to exit", font = ("Courier", 12, "bold") )
s = Screen()
s.exitonclick()