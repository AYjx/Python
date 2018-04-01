#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
ID1 = {20124671:{'name':"WS",'age':20,'birth':918},
      20124668:{'YJX'}}
ID2 = {20124671:{'name':"WS"},20162413020:'YJX'}
print(ID1.setdefault(20124671))    #存在，则获取字典中某个key的Value
dict = ID2.setdefault(2012,"Y")
print(dict)
ID2.setdefault(2012,"Y")    #不存在，则在字典中添加为新key
print(ID2)
print(ID1.fromkeys([1,2,3,5],'xxx'))   #产生新的字典列表中的值作为Key，Value为'xxx'
Dict = {}.fromkeys(['name','age'],'(AN)')
print(Dict)
print(ID1.popitem())       #随机删除一个Key