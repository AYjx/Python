#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
salary = input("Input your salary:")
if salary.isdigit():
      salary = int(salary)
else:
      exit("Invaild data type...")
Welcome_msg = "Welcome to shopping mall".center(50,'-')
print(Welcome_msg)
exit_flag = False

product_list = [
      ('iphone',5988),('mac',9800),('honor',1999),('bike',566),
      ('cloth',188),('coffee',19.9),('ML',62),]

shopping_cart = []
while not exit_flag:
      print("product_list".center(50,'-'))
      for item in enumerate(product_list):
            index = item[0]
            p_name = item[1][0]
            p_price = item[1][1]
            print(index,'.',p_name,p_price)
      user_choice = input("[q=quit,c=check]What do you want?:")
      if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice<len(product_list):
                  p_item = product_list[user_choice]
                  if p_item[1]<=salary:
                        shopping_cart.append(p_item)
                        salary -=p_item[1]
                        print("Added [%s] into shopping cart,your balance is [%s]" %
                              (p_item,salary))
                  else:
                        if user_choice == 'q'or user_choice == 'quit':
                              print("purchased products as below".center(40,'*'))
                              for item in shopping_cart:
                                    print(item)
                              print("end".center(40,'*'))
                              print("your balandce is [%s]"% salary)
                              print("bye")
                              exit_flag = True
                        elif user_choice == 'c'or user_choice == 'check':
                              print("purchased products as below".center(40, '*'))
                              for item in shopping_cart:
                                    print(item)
                              print("end".center(40, '*'))
                              print("your balandce is [%s]" % salary)