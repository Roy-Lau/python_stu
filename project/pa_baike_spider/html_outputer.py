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
			# fout.write("<td>%s</td><td>%s</td><td>%s</td>" % data['url'],data['title'].encode('utf-8'),data['summary'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['url'])
			fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
			fout.write("</tr>")

		fout.write("</html></body></table>")
		fout.close()

