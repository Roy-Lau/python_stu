# -*- coding: utf-8 -*-
#���ӱ��ʽ
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

#�����ɵı���У�����û�м����ͬѧ����ѷ������Ϊ��ɫ��

#��ʾ����ɫ������ <td style="color:red"> ʵ�֡�

def generate_tr(name, score):
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
 
tds = [??? for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>name</th><th>score</th><tr>'
print '\n'.join(tds)
print '</table>'
