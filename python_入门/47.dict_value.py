# -*- coding: utf-8 -*-
#����dict��value

#dict ������һ�� values() ���������������dictת����һ����������value��list�����������ǵ����ľ��� dict��ÿһ�� value��
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
for v in d.values():
    print v

#dict����values()�����⣬����һ�� itervalues() �������� itervalues() ������� values() ����������Ч����ȫһ����
 
print d.itervalues()
for V in d.itervalues():
    print V

#

#�������������кβ�֮ͬ���أ�

#1. values() ����ʵ���ϰ�һ�� dict ת�����˰��� value ��list��

#2. ���� itervalues() ��������ת���������ڵ������������δ� dict ��ȡ�� value������ itervalues() ������ values() ������ʡ������ list ������ڴ档

#3. ��ӡ itervalues() ����������һ�� <dictionary-valueiterator> ������˵����Python�У�for ѭ�������õĵ�������Զ��ֹ list��tuple��str��unicode��dict�ȣ��κοɵ������󶼿���������forѭ�������ڲ���ε�������ͨ�������ù��ġ�

#���һ������˵�Լ��ɵ����������Ǿ�ֱ���� for ѭ��ȥ���������ɼ���������һ�ֳ�������ݲ����������Ե��������ڲ����������κ�Ҫ��
print '------------------------------'
D = {
        'Adan': 95,
        'Lisa': 85,
        'Bart': 59,
        'Paul': 74
    }
sum =0.0
for i in D.itervalues():
    sum = sum + i
print sum / len(D)
