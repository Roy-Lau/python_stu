# -*- coding: utf-8 -*-
d = {
        'Adam': 95,
        'Lisa': 85,
        'bart': 59
        }
print d.items()
for key,value in d.items():
    print key,':',value
print '''С�ջ񣺣������ֿܷ�str��int����������ո�'''

sum = 0.0
for k,v in d.items():
    sum =sum + v
    print k,':',v
print 'average',':',sum/len(d)
