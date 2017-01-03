# -*- coding: utf-8 -*-
# 例
sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print sum
# 题：利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
sum1 = 0
x = 1
n = 1
while True:
    sum1 = x
    x = x + (x * n)  
    if sum1 > 20:
        break
print sum1

