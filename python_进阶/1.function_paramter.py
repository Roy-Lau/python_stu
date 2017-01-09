#-*- coding: utf-8 -*-
#函数式编程
#利用函数式计算平方根
import math
def add(x,y,f):
    return f(x) + f(y)
print add(25,9,math.sqrt)
