#-*- coding: utf-8 -*-
#闭包
#内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
#闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。
def cont():
    fs=[]
    for x in range(1,4):
        def f():
            return x
        fs.append(x)
    return fs
f1,f2,f3 = cont()
print f1
print f2
print f3()
