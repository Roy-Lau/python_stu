# -*- coding: utf-8 -*-
#更新set：由于set储存的是一组不重复的无序元素，因此，更新set主要做两件事。
#一是把新的元素添加到set中，二是把已有元素从set中删除。

print '''作业：针对下面的set，给定一个list，对list中每个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
'''
s = set(['Adan','Lisa','Paul'])
l = ['Adan','Lisa','Bart','Paul']
for x in l:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print s
