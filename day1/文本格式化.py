# -*- coding:utf-8 -*-
# Author：YJX
name = input("input your name:")
age = int(input("input your age:"))
#age = input("input your age:")     #input输入的是字符串
number = input("input your number:")
msg = '''
Information of user %s:
-----------------9
Name :  %s
Age  :  %d
Num  :  %s
------END-------
''' % (name, name, age, number)
print(msg)

