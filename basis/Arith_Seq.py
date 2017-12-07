def checkIndex(key):
	'''键若不是整数，引发TypeError，是负数则引发IndexError'''
	if not isinstance(key, (int, long)): raise TypeError
	if key < 0: raise IndexError
	
class ArithmeticSeq:
	def __init__(self, start = 0, step = 1):
		'''初始化算术序列'''
		self.start = start
		self.step = step
		self.changed = {}

	def __getitem__(self, key):
		checkIndex(key)
		try: return self.changed[key]  #是否修改了
		except KeyError:  
			return self.start + key * self.step  #...计算值

	def __setitem__(self, key, value):
		checkIndex(key)
		self.changed[key] = value   #保存更改后的值