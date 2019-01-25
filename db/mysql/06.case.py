import pymysql
import sys
# 先创建个 account 表格
# CREATE TABLE `account` (
# 	`acctid` INT(11) DEFAULT NULL COMMENT '账户ID',
# 	`money` INT(11) DEFAULT NULL COMMENT '余额'
# 	)ENGINE=INNODB DEFAULT CHARSET=utf8;
#
# 插入 数据
# insert into account (acctid,money) values (1,100);
# insert into account (acctid,money) values (2,100);
#
# 运行方法：
# 执行 文件名 付款id 收款id 金额
# python 06.case.py 1 2 10
#
'''实现银行转账的例子'''

class TransferMoney(object):
	"""转账class for TransferMoney"""
	def __init__(self, conn):
		self.conn = conn
	# 检查账户
	def check_acct_available(self,acctid):
		cursor = self.conn.cursor() # 创建游标
		try:
			sql = "select * from account where acctid=%s" % acctid
			cursor.execute(sql)
			print("检查账户 :\n\t " + sql)
			rs = cursor.fetchall()
			if len(rs) != 1:
				raise Exception("账户%s不存在" % acctid)
		finally:
			cursor.close()
	# 检查付款人是否有足够的转账金额
	def has_enough_money(self,acctid,money):
		cursor = self.conn.cursor()
		try:
			sql = "select * from account where acctid=%s and money>%s" % (acctid,money)
			cursor.execute(sql)
			print("查付款人是否有足够的转账金额:\n\t " + sql)
			rs = cursor.fetchall()
			if len(rs) != 1:
				raise Exception("账户%s余额不足" % acctid)
		finally:
			cursor.close()
	# 付款 操作
	def reduce_money(self,acctid,money):
		cursor = self.conn.cursor()
		try:
			sql = "update account set money=money-%s where acctid=%s" % (money,acctid)
			cursor.execute(sql)
			print("付款 操作:\n\t " + sql)
			rs = cursor.fetchall()
			if cursor.rowcount != 1:
				raise Exception("账户%s扣款失败" % acctid)
		finally:
			cursor.close()
	# 收款 操作
	def add_money(self,acctid,money):
		cursor = self.conn.cursor()
		try:
			sql = "update account set money=money+%s where acctid=%s" % (money,acctid)
			cursor.execute(sql)
			print("收款 操作:\n\t " + sql)
			rs = cursor.fetchall()
			if cursor.rowcount != 1:
				raise Exception("账户%s付款失败" % acctid)
		finally:
			cursor.close()

	# 转账方法
	def transfer(self,source_acctid,target_acctid,money):
		try:
			self.check_acct_available(source_acctid) # 检查账户
			self.check_acct_available(target_acctid) # 检查账户
			self.has_enough_money(source_acctid,money) # 检查付款人是否有足够的转账金额
			self.reduce_money(source_acctid,money) # 付款人减去 money
			self.add_money(target_acctid,money) # 收款人加上 money
			self.conn.commit() # 提交事务
		except Exception as e:
			self.conn.rollback() # 失败，回滚
			raise e

# ======== 主函数
if __name__ == '__main__':
	source_acctid = sys.argv[1] # 付款人id
	target_acctid = sys.argv[2] # 收款人id
	money = sys.argv[3] 		# 金额
	# 连接数据库
	conn = pymysql.connect('139.199.99.154','root','toor','py_test', charset='utf8')
	# 执行转账类，并赋值
	tr_money = TransferMoney(conn)
	try:
		# 调用 transfer 方法
		tr_money.transfer(source_acctid,target_acctid,money)
	except Exception as e:
		print("转账异常： ",str(e))
	finally:
		# 关闭数据库
		conn.close()

