# -*- coding: utf-8 -*-
#在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回

#请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

#如果没有return语句，函数执行完毕后也会返回结果，只是结果为 None。

#return None可以简写为return。

#定义一个square_of_sum函数，它接收一个list，返回list中每个元素平方的和：
def square_of_sum(x):
    k = 0
    for y in x:
        k = k+y*y
    return k
print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])

