# -*- coding: utf-8 -*-
print [m + n for m in 'ABC' for n in '123']

print '''\n翻译成循环代码就像下面这样：'''
l = []
for m in 'ABC':
    for n in '123':
        l.append(m+n)
print l

print '''\n利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。'''

print [(x,y,z) for x in range(1,10) for y in range(1,10) for z in range(1,10) if x == z]

print '\n下面是分解方法——————————————————————\n'
for x in range(1,10):
    for y in range(1,10):
        for z in range(1,10):
            if x == z:
                print x,'',y,'',z
