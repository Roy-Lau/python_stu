# -*- coding: utf-8 -*-
#����Ĭ�ϲ�����
#��ƽ����(���ں����Ĳ����������ҵ�˳��ƥ�䣬����Ĭ�ϲ���ֻ�ܶ����ڱ�������ĺ���)����
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print power(5)
#�붨��һ�� greet() ������������һ��Ĭ�ϲ��������û�д��룬��ӡ 'Hello, world.'��������룬��ӡ 'Hello, xxx.'
def greet(name='world'):
    print 'Hello,' + name
greet()
greet('bart')
