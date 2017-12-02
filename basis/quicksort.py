def quicksort(L):
	less = []
	pivotlist = []
	more = []
	if len(L) <= 1:
		return L
	else:
		pivot = L[0]
		for i in L:
			if i < pivot:
				less.append(i)
			elif i > pivot:
				more.append(i)
			else:
				pivotlist.append(i)

		less = quicksort(less)
		more = quicksort(more)

		return less + pivotlist + more