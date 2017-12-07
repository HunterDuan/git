#用if条件实现归并排序
def MerSort(lists):
	if len(lists) <= 1:
		return lists
	Mid = int(len(lists) / 2)
	left = MerSort(lists[:Mid])
	right = MerSort(lists[Mid:])
	return Merge(left, right)

def Merge(left, right):
	r, l = 0, 0 
	result = []
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	
	remain = left if l < r else right
	k = l if remain == left else r

	while k <len(remain):
		result.append(remain[k])
		k += 1
	return result

#用python中的模块heapq中提供的归并排序方法
from heapq import merge
def merge_sort(seq):
	if len(seq) <= 1:
		return seq
	else:
		middle = len(seq) / 2
		left = merge_sort(seq[:middle])
		right = merge_sort(seq[middle:])
		return list(merge(left, right))

if __name__ == "__main__":
	seq = [1,5,3,6,89,2,1,8,9,43,5,2]
	print(merge_sort(seq))
