# -*- coding: utf-8 -*-
#���ַ���������Ƭ
print 'ABCDEFG'[:3]
print 'ABCDEFG'[-3:]
print 'ABCDEFG'[::2]

#�ַ����и����� upper() ���԰��ַ���ɴ�д��ĸ��
print 'abc'.upper()

#��ҵ���������������ĸ����ɴ�д�������һ��������������һ���ַ�����Ȼ�󷵻�һ��������ĸ��ɴ�д���ַ���
def firstcharupper(s):
    return s[:1].upper() +  s[1:len(s)]
print firstcharupper('hello')
print firstcharupper('sunday')
print firstcharupper('september')
