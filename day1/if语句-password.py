# -*- coding:utf-8 -*-
# Author：YJX
user = 'test'
passwd= '2016'
username = input("username:")
password = input("password:")
if user == username and passwd == password:
    print("Welcome login...")
else:
    print("Invalid username or password...")