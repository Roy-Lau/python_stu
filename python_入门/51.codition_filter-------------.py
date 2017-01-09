# -*- coding: utf-8 -*-
print [x * x for x in range(1,11)]

print [x * x for x in range(1,11) if x % 2 == 0]

#请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。

#提示：
#1. isinstance(x, str) 可以判断变量 x 是否是字符串；
#2. 字符串的 upper() 方法可以返回大写的字母。
def touppers(angs):
    for k in angs:
        return k
#       if isinstance(k, str):
#           return k[:1].upper()
print touppers(['hello','world',101])

#为什么在函数式内 for in 遍历数组失败（只出来一个）
