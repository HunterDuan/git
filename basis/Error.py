#异常的输出
'''while True:
	try:
		x = input('Enter the first number: ')
		y = input('Enter the second number: ')
		value = x / y
		print('x / y is %d')%value
	except Exception as E:  #包括任何错误的输出
		print('Invalid input: %s')%E
		print('Please input again!')
	else:
		break

#捕捉常见异常
try:
	x = input('Enter the first number: ')
	y = input('Enter the second number: ')
	print('%d')%(x/y)
except (ZeroDivisionError, TypeError) as e:
	print('%s')%e'''

#控制异常的屏蔽输出
class Errortest():
	ET = False
	def calc(self, expr):
		try:
			return eval(expr)
		except ZeroDivisionError:
			if self.ET: 
				print('Division by zero is illegal')
			else:
				raise   #利用raise可以屏蔽ZeroDivionError异常

