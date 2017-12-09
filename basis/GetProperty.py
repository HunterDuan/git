class Rectangle():
	def __init__(self):
		self.width = 0
		self.height = 0
	def setsize(self, size):
		self.width,self.height = size
	def getsize(self):
		return self.width, self.height

#使用property函数实现隐藏属性
__metaclass__ = type #子类化Object或增加__metaclass__=type来使用property函数
class Rectangle():
	def __init__(self):
		self.width = 0
		self.height = 0
	def setsize(self, size):
		self.width,self.height = size
	def getsize(self):
		return self.width, self.height
	size = property(getsize, setsize)

#使用@property来装饰
__metaclass__ = type #增加了该语句后新设置的变量可以被获取
class Rectangle():
	def __init__(self):
		self.width = 0
		self.height = 0
	@property
	def size(self):
		return self.width, self.height	
	@size.setter
	def size(self, size):
		self.width,self.height = size
