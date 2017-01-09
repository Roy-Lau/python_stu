#-*- coding: utf-8 -*-
#map()函数
#map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
def f(x):
    return x*x
print map(f,[1,2,3,4,5,6,7,8,9,])

def format_name(s):
    return s[:1].upper()+s[1:len(s)].lower()
print map(format_name,['adam','LISA','bart'])
