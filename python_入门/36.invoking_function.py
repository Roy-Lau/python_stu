# -*- coding: utf-8 -*-
#调用函数：python函数官网——http://docs.python.org/2/library/functions.html#abs
#交互式命令行通过help(abs)可以查看abs的帮助信息！
print '''abs函数例：'''
A1 = abs(100)
A2 = abs(-20)
A3 = abs(12.34)
print A1
print A2
print A3

print '''比较函数cmp(x,y)需要两个参数，如果想x<y,返回-1.如果x==y，返回0.如果x>y,返回1：'''
C1 = cmp(1,2)
C2 = cmp(2,1)
C3 = cmp(3,3)

print C1
print C2
print C3

print '''数据类型转换函数int(),比如int()函数可以把其他的数据类型转换成整数。'''
I1 = int('123')
I2 = int(12.34)
print I1
print I2

print '''str()字符串函数 例：'''
S1 = str(123)
S2 = str(1.23)
print S1
print S2

print '''计算1*1+2*2...+100*100'''
print '''sum()函数：list里的上一位加下一位'''

L = range(100*100+1)
#print L
print sum(L)
