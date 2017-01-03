# -*- coding: utf-8 -*-
#定义默认参数：
#求平方，(由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面)例：
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print power(5)
#请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
def greet(name='world'):
    print 'Hello,' + name
greet()
greet('bart')
