# -*- coding:utf-8 -*-
# Author：YJX
real_age = 20

for i in range(10):
    if i>=3:break
    guess_age = int(input("guess_age:"))
    if guess_age > real_age:
        print("try a smaller")
    elif guess_age < real_age :
        print("try a bigger")
    else:
        print("got it...")
        break