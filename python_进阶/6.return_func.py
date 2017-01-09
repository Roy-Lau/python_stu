#-*- coding: utf-8 -*-
#返回函数
#Python的函数不但可以返回int、str、list、dict等数据类型，还可以返回函数！

#请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
    def lazy_prod(lst):
        return lst*lst
    return lazy_prod
f = calc_prod([1,2,3,4])
print f
print f()

#这一章似是而非，没学明白！
