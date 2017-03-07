#-*- coding: utf-8 -*-
#创建实例属性

class Person(object):
    pass
#虽然可以通过Person类创建出xiaoming、xiaohong等实例，但是这些实例看上除了地址不同外，没有什么其他不同。在现实世界中，区分xiaoming、xiaohong要依靠他们各自的名字、性别、生日等属性。

#如何让每个实例拥有各自不同的属性？由于Python是动态语言，对每一个实例，都可以直接给他们的属性赋值，例如，给xiaoming这个实例加上name、gender和birth属性：

xiaoming = Person()
xiaoming.name = 'Xiao Ming'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1'

#给xiaohong加上的属性不一定要和xiaoming相同：

xiaohong = Person()
xiaohong.name = 'Xiao Hong'
xiaohong.school = 'No. 1 High School'
xiaohong.grade = 2

#实例的属性可以像普通变量一样进行操作：

xiaohong.grade = xiaohong.grade + 1

class person(object):
    pass
p1 = person()
p1.name = 'bart'
 
p2 = person()
p2.name = 'adam'
 
p3 = person()
p3.name = 'lisa'
 
l1 = [p1, p2, p3]
for x in l1:
    print sorted(x.name) 
