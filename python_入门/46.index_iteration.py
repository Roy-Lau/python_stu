# -*- coding: utf-8 -*-
#zip()�������԰����� list ���һ�� list��
print zip([10, 20, 30], ['A', 'B', 'C'])

#��������:enumerate(list)
l = ['adam', 'lisa', 'bart', 'paul']
for index, name in enumerate(l):
    print index+1, '-', name

print '-------������ÿһ��Ԫ��ʵ������һ��tuple-----------'
for t in enumerate(l):
    index = t[0]
    name = t[1]
    print index, '-', name
