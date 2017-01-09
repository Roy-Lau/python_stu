#-*- coding: utf-8 -*-

#装饰器
def f1(x):
    return x*2

def new_fn(f):
    def f3(x):
        print 'call'+f.__name__+'()'
        return f(x)
    return f3
f1 = new_fn(f1) #这个调用了new_fn里面的f1，所以打印出了callf1()
print f1(5)     #这个打印的是最上边的f1()---------10

@new_fn          #@new_fn相当于将上边的new_fn()装饰到了f2上
def f2(x):
    return x*3
print f2(5)      #这个打印出了f2()-----------15
