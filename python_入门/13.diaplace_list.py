# -*- coding: utf-8 -*-
L = ['Adam','Lisa','Bart']
L[2] = 'Paul'
print L
print '在一次考试后，Bart同学意外取得第一，而Adam同学考了倒数第一。请通过对list的索引赋值，生成新的排名。'
L1 = ['Adam','Lisa','Bart']
L1[0] = L1[-1]
L1[-1] = 'Adam'
print L1

print '还有更简单的 倒一 和 正一 互换'
L2 = ['Adam','Lisa','Bart']
L2 = [L2[-1],'Lisa',L2[0]]
print L2