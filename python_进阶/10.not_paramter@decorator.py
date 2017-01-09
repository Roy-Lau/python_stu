#-*- coding: utf-8 -*- 
#编写无参数装饰器
def log(f):
    def fn(x):
        print 'call '+ f.__name__+'()...'
        return f(x)
    return fn
@log
def fac(n):
    return reduce(lambda x,y: x+y,range(1, n+1))
print fac(10)


import time
def performance(f):
    def times(t):
        print time
        return f(t)
    return times

@performance        #将performance装饰到下面
def factorial(n):
    return reduce(lambda x,y: x*y,range(1, n+1))
#factorial = performance(factorial)
print factorial(10)
