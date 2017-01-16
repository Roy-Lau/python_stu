#-*- coding: utf-8 -*- 
#带参数的装饰器
def log(prefix):
    def log_decorator(f):
        def weapper(*args, **kw):
            print '[%s] %s()...' %(prefix,f.__name__)
            return f(*args, **kw)
        return weapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()

#对于上面这种3层嵌套的decorator定义，可以先把它拆开：
#标准decorator
def log_decorators(f):
    def wrappers(*args, **kw):
        print '[%s] %s()...' % (prefix, f.__name__)
        return f(*args, **kw)
    return wrappers
#return log_decorators  ???

#返回decorator:
def log(prefix):
    return log_decorator(f)

#拆开以后会发现，调用会失败，因为在3层嵌套的decorator定义中，最内层的wrapper引用了最外层的参数prefix，所以，把一个闭包拆成普通的函数调用会比较困难。不支持闭包的编程语言要实现同样的功能就需要更多的代码。

print '''-------------作业------------'''
import time

def performance(unit):
    def times(t):
#       print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print time.time()
        return unit(t)
    return times

@performance('ms')
def factormance(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

print factorial(10)

#time有问题遗留！(作业没完成)
