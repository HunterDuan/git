import urllib.request
def use_proxy(url,proxy_addr):
	proxy = urllib.request.ProxyHandler({"http":proxy_addr})
	opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)
	data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
	return data

proxy_addr = "14.118.254.164:6666"
url = "http://www.baidu.com"
data = use_proxy(url, proxy_addr)
print(len(data))