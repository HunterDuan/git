'''爬取咸鱼的图片'''
import urllib.request
import re
searchID = '50100401'#搜索词的ID，
search = urllib.request.quote(searchID)#若是中文搜索词，则用quote转化
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
imageurl = []
for i in range(0,2):
    url = "https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.26cd2979C6oQRJ&catid="+searchID+"&st_trust=1&page="+str(i+1)
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat = '//(img.alicdn.com/bao/uploaded/.*?)"'
    imagelist = re.compile(pat).findall(data)
    for j in range(0,len(imagelist)):
    	thisimg = imagelist[j]
    	thisimgurl = "http://" + thisimg
    	name = "F:/crawl/" + str(i) + str(j) + ".jpg"
    	urllib.request.urlretrieve(thisimgurl, filename = name)
