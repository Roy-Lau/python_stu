#-*- coding: utf-8 -*-
#动态导入模块
#如果导入的模块不存在，Python解释器会报 ImportError 错误：比如下面这个模块-

#import something

#有的时候，两个不同的模块提供了相同的功能，比如 StringIO 和 cStringIO 都提供了StringIO这个功能。
#这是因为Python是动态语言，解释执行，因此Python代码运行速度慢。
#如果要提高Python代码的运行速度，最简单的方法是把某些关键函数用 C 语言重写，这样就能大大提高执行速度。
#同样的功能，StringIO 是纯Python代码编写的，而 cStringIO 部分函数是 C 写的，因此 cStringIO 运行速度更快。
#利用ImportError错误，我们经常在Python中动态导入模块：

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

#上述代码先尝试从cStringIO导入，如果失败了（比如cStringIO没有被安装），再尝试从StringIO导入。这样，如果cStringIO模块存在，则我们将获得更快的运行速度，如果cStringIO不存在，则顶多代码运行速度会变慢，但不会影响代码的正常执行。

#try 的作用是捕获错误，并在捕获到指定错误时执行 except 语句。
#作业
try:
    import json
except ImportError:
    import simplejson
print json.dumps({'python':'2.7'})
