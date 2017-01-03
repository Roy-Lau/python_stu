# -*- coding: utf-8 -*-
#set的特点：set的内部和dict很像，唯一的区别是不储存value，以此，判断一个元素是否在set中速度很快。
#set储存的元素和dict的key类似，必须是不变的对象，因此，任何可变对象是不能放入set中的。
#最后，set储存的元素也是没有顺序的。
months = set(['January','February','March','Aprll','May','June','july','August','September','October','November','December'])

x1 = 'February'
x2 = 'sun'

if x1 in months:
    print 'x1 : ok'
else:
    print 'x1 : error'

if x2 in months:
    print 'x2 : ok'
else:
    print 'x2 : error'
