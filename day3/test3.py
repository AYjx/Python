#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
#3、关闭文件

with open('df3','r',encoding='utf-8') as f1,open('df03','w',encoding='utf-8') as f2:
    #df3中的内容只读并做为f1，对df03中只写并做为f2
    times = 0#行数
    for line in f1:
        new_str = line.replace("ddd","admin")
        #将df3中的文件替换df03中的文件
        times += 1
        if times>3:#行数大于3 则停止替换
            break
        else:
            f2.write(new_str)
    pass