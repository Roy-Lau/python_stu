# -*- coding: UTF-8 -*-
raw = r'\(~_~)/ \(~_~)/'	
raw1 = '''Line 1
		  Line 2
		  Line 3'''
print raw
print raw1

work = '\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'
work1 = '''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''
print work + '————————————————————这是目标'
print work1 + '————————————————————这是结果'


# 如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。
# 为了避免这种情况，我们可以在字符串前面加个前缀 r ，表示这是一个 raw 字符串，里面的字符就不需要转义了

# 如果要表示多行字符串，可以用'''...'''表示：









