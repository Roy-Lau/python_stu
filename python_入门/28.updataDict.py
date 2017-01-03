# -*- coding: utf-8 -*-
d = {
        95: 'Adam',
        85: 'Lisa',
        59: 'Bart'
    }
d[95] = 'qiang'
print d
#将所有key值替换成value值, 思考怎么加value值替换成key值
for k in d:
    d[k] = k
print d
