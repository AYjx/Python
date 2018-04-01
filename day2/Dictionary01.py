#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
ID = {20124671:{'name':"WS",'age':20,'birth':918},
      #Key:Value(其中Value可以是字典，字符串，数字等)
      20124668:'YJX',
      20124670:{'name':"GJH",'age':21,'birth':721},
      20124669:{'name':"JP",'age':18,'birth':801}
      }
ID1 = {20124671:{'name':"WS",'age':20,'birth':918},
      20124668:'YJX'}
ID2 = {20124671:{'name':"WS"},20162413020:'YJX'}

ID[20124670]['name'] = 'xxx'    #修改
ID[20124670]['addr'] = 'JX'     #添加
ID[20124671].pop('age')          #删除
del ID[20124670]['age']         #删除
ID1.update(ID2)  #将字典ID2中的内容更新到字典ID，对比键Key,
                # 原字典中没有的就添加，已有的就更改
print(ID[20124670])
print(ID[20124671])
print(ID1)