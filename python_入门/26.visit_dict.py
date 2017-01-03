# -*- coding: utf-8 -*-
d = {
        'adan': 95,
        'lisa': 85,
        'bart': 50
        }
print d.get('adan')
print d.get('lisa')
print d.get('bart')

print '''两种不同的方法判断key值是否存在'''

if 'adan' in d:
    print d['adan']

print '''打印的key值'''
for key in d:
    print key
