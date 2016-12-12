 # -*- coding: utf-8 -*-
print True and True   # ==> True
print True and False   # ==> False
print False and True   # ==> False
print False and False   # ==> False
print '与运算\n'

print True or True   # ==> True
print True or False   # ==> True
print False or True   # ==> True
print False or False   # ==> False
print '或运算\n'

print not True   # ==> False
print not False   # ==> True
print '非运算\n'

a = True
print a and 'a=T' or 'a=F'
print 'Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True\n'
print '''\t要解释上述结果，又涉及到 and 和 or 运算的一条重要法则：短路计算。
1. 在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，因此返回 a；如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b。
2. 在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。
所以Python解释器在做布尔运算时，只要能提前确定计算结果，它就不会往后算了，直接返回结果。'''

a = 'python'
print 'hello,', a or 'word'

b = ''
print 'hello,', b or 'word'
