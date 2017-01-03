# -*- coding: utf-8 -*-
#对字符串进行切片
print 'ABCDEFG'[:3]
print 'ABCDEFG'[-3:]
print 'ABCDEFG'[::2]

#字符串有个方法 upper() 可以把字符变成大写字母：
print 'abc'.upper()

#作业：但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串
def firstcharupper(s):
    return s[:1].upper() +  s[1:len(s)]
print firstcharupper('hello')
print firstcharupper('sunday')
print firstcharupper('september')
