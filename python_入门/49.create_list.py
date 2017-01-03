# -*- coding: utf-8 -*-
#生成列表
#要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，我们可以用range(1, 11)：
print range(1, 11)

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
l = []
for x in range(1,11):
    l.append(x * x)
print l

print '''但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：'''

print [x * x for x in range(1,11)]

print range(1,100,2)

#请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print [x * (x+1) for x in range(1,101,2)]

