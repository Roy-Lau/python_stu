import pymysql

# 本文件名讲解：
# i insert 插入
# u update 更新
# d delete 删除

# 连接数据库
conn = pymysql.connect('139.199.99.154','root','toor','py_test', charset='utf8')


# 创建游标
cursor = conn.cursor()

# 数据库查询语句
# 插入userid为1的这行，username为name1(如果userid为1这行已有数据，会报错)
sql_insert = "insert into user (userid,username) values(1,'name1');"
# 将userid等于1的username改为 nam_eone
sql_update = "update user set username='name_one' where userid=1;"
# 删除userid小于3的数据
sql_delete = "delete from user where userid<3;"

try:
	# 执行sql
	cursor.execute(sql_insert)
	print("查看上面的SQL执行，影响了几行数据: ",cursor.rowcount)
	cursor.execute(sql_update)
	print("查看上面的SQL执行，影响了几行数据: ",cursor.rowcount)
	cursor.execute(sql_delete)
	print("查看上面的SQL执行，影响了几行数据: ",cursor.rowcount)
	# 提交事务
	conn.commit()
except Exception as e:
	print(e)
	# 回滚事务
	conn.rollback()


# 关闭数据库
conn.close()
# 关闭游标
cursor.close()
