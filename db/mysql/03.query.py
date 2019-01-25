import pymysql

# 想查询，先创建


# 连接数据库
conn = pymysql.connect('139.199.99.154','root','toor','py_test', charset='utf8')

# 创建游标
cursor = conn.cursor()

#======= 先创建个 user 表格
sql_create = '''CREATE TABLE `user` (
				`userid` INT(11) NOT NULL AUTO_INCREMENT,
				`username` VARCHAR(100) DEFAULT NULL,
				PRIMARY KEY (`userid`)
				)ENGINE=INNODB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;'''

try:
	cursor.execute(sql_create)
	# 提交事务
	conn.commit()
except Exception as e:
	print("CREATE ERROR >>",e)
	# 回滚事务
	conn.rollback()

#====== 插入10条数据
for n in range(10):
	try:
		cursor.execute("insert into user (userid,username) values(%s,'names');" % n)
		# 提交事务
		conn.commit()
	except Exception as e:
		print("INSERT ERROR >>",e)
		# 回滚事务
		conn.rollback()

#======== 数据库查询语句
sql = "select * from user;"
# 执行 sql
cursor.execute(sql)

# 查询 表格总行数
print("表格总行数:",cursor.rowcount)

# 查询 第一条数据
rs = cursor.fetchone()
print("第一条数据是：",rs)

# 获取 三条数据
rs = cursor.fetchmany(3)
print("获取三条数据：",rs)

# 查询剩余的所有数据
rs = cursor.fetchall()
print("查询剩余的所有数据：",rs)

# 关闭数据库
conn.close()
# 关闭游标
cursor.close()
