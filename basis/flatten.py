'''def flatten(nested):
	result = []
	try:
		try:
			nested + ''
		except TypeError: pass
		else: raise TypeError
		for sublist in nested:
			for element in flatten(sublist):
				result.append(element)
	except TypeError:
		result.append(nested)
	return result'''

#递归生成器方法
def flatten2(nested): 
	try:  
		try: nested + ''   #若nested+''表达式引发异常则会pass进入下面的循环
		except TypeError: pass  
		else: raise TypeError  #若表达式没引发TypeError,在内层try语句中引发异常
		for sublist in nested:
			for element	 in flatten2(sublist):
				yield element
	except TypeError:
		yield nested
