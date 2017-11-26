'''经典的两个递归'''
def factorial(n):    #使用循环来做n的阶乘
	result = n 
	for i in range(1,n):
		result *= n
	return result

def factorial2(n):  #递归做阶乘
	if n == 1:
		return 1
	else:
		return n * factorial2(n - 1)

def power(x,n):     #用循环来实现x的n乘方
	result = 1
	for i in range(1,n):
		result *= x
	return result
def power2(x,n):	#用递归来实现乘方
	if n == 0:
		return 1
	else:
		return x * power2(x, n - 1)
