#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
LOGIN_USER = {'is_login':False} # 字典
def outer(func):
    def inner(*args,**kwargs):
        if LOGIN_USER['is_login']:
            r = func()
            return r
        else:
            print('请登录')
    return  inner

@outer
def order():
        print("%s登录成功" % LOGIN_USER['current_user'])
@outer
def passward():
        print("%s登录成功" % LOGIN_USER['current_user'])
@outer
def manager():
        print("%s登录成功" % LOGIN_USER['current_user'])

def login(user,pwd):
    if user == 'YJX' and pwd =='123':
        LOGIN_USER['is_login'] = True
        LOGIN_USER['current_user'] = user
        manager()
def main():
    while True:
        inp = input("1:后台管理；2：登录\n")
        if inp == '1':
            manager()
        elif inp == '2':
            username = input("请输入用户名")
            pwd = input("请输入密码")
            login(username, pwd)
main()