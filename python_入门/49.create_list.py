# -*- coding: utf-8 -*-
#�����б�
#Ҫ����list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]�����ǿ�����range(1, 11)��
print range(1, 11)

#�����Ҫ����[1x1, 2x2, 3x3, ..., 10x10]��ô��������һ��ѭ����
l = []
for x in range(1,11):
    l.append(x * x)
print l

print '''����ѭ��̫���������б�����ʽ�������һ��������ѭ�����������list��'''

print [x * x for x in range(1,11)]

print range(1,100,2)

#�������б�����ʽ�����б� [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print [x * (x+1) for x in range(1,101,2)]

