#-*- coding: utf-8 -*-
#filter()函数
#filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
def is_add(x):
    return x % 2 ==1
print filter(is_add,[1,2,3,4,5,6,7,8,9,10])

#利用filter()，可以完成很多有用的功能，例如，删除 None 或者空字符串：
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

#注意: s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
#当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')，如下：

a = '     123'
print a.strip()

a='\t\t123\r\n'
print a.strip()
#作业：请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
import math
def is_sqr(x):
    return x == math.sqrt(x)
print filter(is_sqr, range(1,101))

for y in range(1,101):
    print y == math.sqrt(y)
