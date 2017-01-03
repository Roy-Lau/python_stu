# -*- coding: utf-8 -*-
#倒序切片
l = ['Adam','Lisa','Bart','Paul']
print l[-2:]
print l[:-2]
print l[-3:-1]
print l[-4:-1:2]
#记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引

#作业：最后10个数，最后10个5的倍数；
L = range(1,101)
k=L[-10:]
print k
print k[4::5]
