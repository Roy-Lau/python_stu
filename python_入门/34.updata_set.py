# -*- coding: utf-8 -*-
#����set������set�������һ�鲻�ظ�������Ԫ�أ���ˣ�����set��Ҫ�������¡�
#һ�ǰ��µ�Ԫ����ӵ�set�У����ǰ�����Ԫ�ش�set��ɾ����

print '''��ҵ����������set������һ��list����list��ÿ��Ԫ�أ������set�У��ͽ���ɾ�����������set�У�����ӽ�ȥ��
'''
s = set(['Adan','Lisa','Paul'])
l = ['Adan','Lisa','Bart','Paul']
for x in l:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print s
