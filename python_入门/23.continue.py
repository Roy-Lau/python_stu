# -*- coding: utf-8 -*-

# 对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
# sum = 0
# x = 1
# while True:
#     sum = sum + x
#     x = x + 1
#     if x > 100:
#         break
# print sum
sum = 0
x = 0
y = 0
while True:
    x = x + 1
    if x > 100:
        break
    y = y + 2
    if x == y:
        continue
    sum = sum + x 
    print sum
