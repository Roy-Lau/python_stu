# -*- coding: utf-8 -*-
#复杂表达式
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

tds = [
        '<tr><td>%s</td><td>%s</td></th>'
        %(name,score)
        for name,score in d.iteritems()
        ]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

#在生成的表格中，对于没有及格的同学，请把分数标记为红色。

#提示：红色可以用 <td style="color:red"> 实现。

def generate_tr(name, score):
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
 
tds = [??? for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>name</th><th>score</th><tr>'
print '\n'.join(tds)
print '</table>'
