#查找排序后的数字在列表中的位置
def search(sequence, number, lower = 0, upper = None):
	sequence = sorted(sequence)
	if upper is None: upper = len(sequence) - 1
	if lower == upper:
		assert number == sequence[upper], 'The equal of upper and lower'
		return upper
	else:
		middle = (lower	+ upper) // 2
		if number > sequence[middle]:
			return search(sequence, number, middle + 1, upper)
		else:
			return search(sequence, number, lower, middle)

#收集参数（*arg和**arg）
def print_param(**args):
	print (args)
print_param(x = 2, y = 13, z = 5) # 返回字典

def print_param2(*args):
	print (args)
print_param2(1,2,3)  # 返回元组