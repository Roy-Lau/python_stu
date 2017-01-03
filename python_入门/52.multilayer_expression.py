# -*- coding: utf-8 -*-
print [m +n for m in 'ABC' for n in '123']

#翻译成循环代码就像下面这样：
l = []
for m in 'ABC':
    for n in '123':
        l.append(m+n)
print l

#利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。

print [???]
