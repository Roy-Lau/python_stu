# coding:utf8

class HtmlOutputer(object):
	""" html 输出器 """
	def __init__(self):
		self.datas = []

	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	# ascii
	def output_html(self):
		fout = open('output.html','w')

		fout.write("<html><body><table border=1>")
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td><a href='"+data['url']+"'>%s</td>" % data['title'])
			fout.write("<td>%s</td>" % data['summary'])
			fout.write("</tr>")

		fout.write("</html></body></table>")
		fout.close()

