#子类化一个内建list类型，间接地将Object子类化了，还可以子类化字典和字符串
class CounterList(list):
	def __init__(self, *args):
		super(CounterList, self).__init__(*args) #继承list父类
		self.counter = 0
	def __getitem__(self, index):
		self.counter += 1
		return super(CounterList, self).__getitem__(index)