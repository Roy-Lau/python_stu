# -*- coding: utf-8 -*-
d = {
        95: 'Adam',
        85: 'Lisa',
        59: 'Bart'
    }
d[95] = 'qiang'
print d
#������keyֵ�滻��valueֵ, ˼����ô��valueֵ�滻��keyֵ
for k in d:
    d[k] = k
print d
