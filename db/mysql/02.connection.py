import pymysql

# 连接数据库
conn = pymysql.connect(
	host = '139.199.99.154',
	port = 3306,
	user = 'root',
	passwd = 'toor',
	db = 'py_test',
	charset = 'utf8'
	)
# 可以简写为
# conn = pymysql.connect('139.199.99.154','root','toor','py_test', charset='utf8')

# 创建游标
cursor = conn.cursor()

# 打印连接
print(conn)
# 打印游标
print(cursor)

# 关闭连接
conn.close()
# 关闭游标
cursor.close()
