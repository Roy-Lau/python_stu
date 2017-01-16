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
        print time.time(),'S'   #打印1970纪元到现在的秒数
        print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) #转化为正常的时间格式
        return f(t)
    return times

@performance        #将performance装饰到下面
def factorial(n):
    return reduce(lambda x,y: x*y,range(1, n+1))
factorial = performance(factorial)      #打印1970纪元到现在的秒数
print factorial(10)
