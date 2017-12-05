def Merge_Sort(Lst):  #应用list.pop方法进行归并排序
	if len(Lst) <= 1:
		return Lst
	def Merge(left, right):
		Merge_list = []
		while left and right:
			Merged_list.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
		while left:
			Merged_list.append(left.pop(0))	
		while right:
			Merged_list.append(right(0))
		return Merged_list

	middle = int(len(Lst) / 2)
	left = Merge_Sort(Lst[:middle])
	right = Merge_Sort(Lst[middle:])
	return Merge(left, right)