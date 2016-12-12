# -*- coding: utf-8 -*-
print '''有的时候，一个if...else ...还不够用。比如，根据年龄的划分：
	条件1：18岁或以上：adult
	条件2：6岁或以上：teenager
	条件3：6岁以下：kid'''
age = 8
if age >= 18:
	print '成年'
elif age >= 6:
	print '青少年','-----------------------------'
elif age >= 3:
	print '幼年'
else:
	print 'baby'	

print '''如果按照分数划定结果：
    90分或以上：excellent
    80分或以上：good
    60分或以上：passed
    60分以下：failed'''	

score = 8
 
if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed-------------------------------'

