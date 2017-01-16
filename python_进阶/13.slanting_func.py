#-*- coding: utf-8 -*- 
#偏函数
print int('789')
print int('666', base=8)   ,'8进制打印'
print int('888', 16)       ,'16进制打印'

def int2(x,base=2):
    return int(x,base)
print int2('110110')
print int2('101010')

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int3 = functools.partial(int,base=2)
print int3('110110')
print int3('101010')
#作业(忽略大小写排序)
sorted_ignore_case = functools.partial(sorted)
print sorted_ignore_case(['bob','about','zoo','Credit'])
