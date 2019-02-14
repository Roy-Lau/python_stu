# coding:utf8

class HtmlOutputer(object):
	""" html 输出器 """
	def __init__(self):
		self.data = []

	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	# ascii
	def collect_data(self):
		fout = open('output.html','w')

		fout.write("<html><body><table>")
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td><td>%s</td><td>%s</td>" % data['url'],data['title'].encode('utf-8'),data['summary'].encode('utf-8'))
			fout.write("</tr>")

		fout.write("</html></body></table>")
		fout.close()

