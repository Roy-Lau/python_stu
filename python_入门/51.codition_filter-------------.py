# -*- coding: utf-8 -*-
print [x*x for x in range(1,11)]

print [x * x for x in range(1,11) if x % 2 == 0]

#���дһ��������������һ�� list��Ȼ���list�е������ַ�����ɴ�д�󷵻أ����ַ���Ԫ�ؽ������ԡ�

#��ʾ��
#1. isinstance(x, str) �����жϱ��� x �Ƿ����ַ�����
#2. �ַ����� upper() �������Է��ش�д����ĸ��
def touppers(l):
    for k in l:
        return k
#       if isinstance(k, str):
#           return k[:1],upper()
print touppers(['hello','world',101])

