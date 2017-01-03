# -*- coding: utf-8 -*-
#对list进行切片：
L = ['adam','Lisa','Bart','paul']
print L[0:3]
print L[:3]
print L[1:3]
print L[:]
print L[::2]
#作业：利用切片取出 1.前10个数，2.3的倍数，3.不大于50的5的倍数
l = range(1,101)
print l[:10]
print l[2::3]
k=l[:50]
print k[4::5]
