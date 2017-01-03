# -*- coding: utf-8 -*-
#返回多值：
#编写一个函数，返回一元二次方程的解，方程式：ax平方+bx+x =0；
import math
def quadratic_equation(a,b,c):
    x=1
    sqrt= math.sqrt(a*x)
    y = sqrt + b*x + c
    return sqrt,y
print quadratic_equation(2,3,0)
print quadratic_equation(1,-6,5)

#写出来了，但是，不太明白！
