# =*= coding: utf-8 -*-
t = ('a', 'b', ['A', 'B'])
print t[2]

t[2][0] = 'X'
t[2][1] = 'Y'
print t

print '''\t由于 t 包含一个list元素，导致tuple的内容是可变的。能否修改上述代码，让tuple内容不可变？t1 = ('a', 'b', ['a','b'])'''
t1 = ('a', 'b', ['A', 'B'])
# ...........
print t1