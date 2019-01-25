import pymysql


# 连接数据库
conn = pymysql.connect('139.199.99.154','root','toor','py_test', charset='utf8')

# 创建游标
cursor = conn.cursor()
# 数据库查询语句
sql = "select * from user;"
# 执行
cursor.execute(sql)

# 获取全部数据
rs = cursor.fetchall()
# 循环打印
for row in rs:
	print("userid=%s,usernanme=%s" % row)

# 关闭数据库
conn.close()
# 关闭游标
cursor.close()
