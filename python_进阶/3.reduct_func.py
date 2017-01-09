#-*- coding: utf-8 -*-
#reduce()函数
#reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
def f(x,y):
    return x + y
print '''先计算头两个元素：f(1, 3)，结果为4；
再把结果和第3个元素计算：f(4, 5)，结果为9；
再把结果和第4个元素计算：f(9, 7)，结果为16；
再把结果和第5个元素计算：f(16, 9)，结果为25；
由于没有更多的元素了，计算结束，返回结果25。'''
print reduce(f,[1,3,5,7,9])
print reduce(f,[1,3,5,7,9],100)
#计算初始值和第一个元素：f(100, 1)，结果为101。
print '''Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：'''
def prod(x,y):
    return x * y
print reduce(prod,[2,4,6,8])
