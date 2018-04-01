# -*- coding:utf-8 -*-
# Author：YJX
def main():
    x_str=input('请输入正整数x=')
    x=int(x_str)
    y_str=input('请输入正整数y=')
    y=int(y_str)
    print(x,'和',y,'的最大公约数是：', GCD(x,y))

def GCD(x,y):
    if x>y: a=x;b=y
    else:   a=y;b=x
    if a%b ==0: return(b)
    return(GCD(a%b,b))

if(__name__=="__main__"):
   main()