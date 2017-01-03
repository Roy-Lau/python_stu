# -*- coding: utf-8 -*-
#zip()函数可以把两个 list 变成一个 list：
print zip([10, 20, 30], ['A', 'B', 'C'])

#引索迭代:enumerate(list)
l = ['adam', 'lisa', 'bart', 'paul']
for index, name in enumerate(l):
    print index+1, '-', name

print '-------迭代的每一个元素实际上是一个tuple-----------'
for t in enumerate(l):
    index = t[0]
    name = t[1]
    print index, '-', name
