def search(sequence, number, lower = 0, upper = None):
	if upper is None: upper = len(sequence) - 1
	if lower == upper:
		assert number == sequence[upper], 'The equal of upper and lower'
		return upper
	else:
		middle = (lower	+ upper) // 2
		if middle > sequence[middle]:
			return search(sequence, number, middle + 1, upper)
		else:
			return search(sequence, number, lower, middle)