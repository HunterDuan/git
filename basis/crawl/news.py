'''爬取新浪新闻的各个页面'''
import urllib.request
import re
data = urllib.request.urlopen("http://news.sina.com.cn/").read()
data2 = data.decode("utf-8", "ignore")
pat = 'href="(http://news.sina.com.cn/.*?)"'
allurl = re.compile(pat).findall(data2)
for i in range(0,len(allurl)):
	try:
		print('第'+str(i)+'次爬取')
		thisurl = allurl[i]
		name = "F:/crawl/"+str(i)+".html"
		urllib.request.urlretrieve(thisurl, filename = name)
		print('----成功-----')
	except urllib.error.URLError as e:
		if hasattr(e, "code"):
			print(e.code)
		if hasattr(e, "reason"):
			print(e.reason)
