'''class Solution:
    def twosum(self, num, target):
    	sorted_num = sorted(num)
    	left = 0
    	right = len(num) - 1
    	res = []

    	while left < right:
    		sum = sorted_num[left] + sorted_num[right]
    		if sum == target:
    			break;
    		elif sum > target:
    			right -= 1
    		else:
    			left += 1
    		if left	 == right:
    			return -1, -1
    		else:
    			pos1 = num.index(sorted_num[left] + 1) 
    			pos2 = num.index(sorted_num[right] + 1)
    			if pos1 == pos2:
    				pos2 = num[pos1:].index(sorted_num[right] + pos1 + 1)
    				return min(pos1, pos2), max(pos1, pos2)

s = Solution()
print (s.twosum([-1, 2, 3, -2], 0))'''

class Solution():
	def twosum(self, num, target = 0):
		if len(num) <2:
			return None
		num = sorted(num)

		ret = []
		left = 0
		right = len(num) - 1
		Sum = 0

		while left < right:
			Sum = num[left] + num[right]
			if Sum < target:
				left += 1
			elif Sum >target:
				right -= 1
			else:
				ret.append([num[left], num[right]])
				left += 1
				right -= 1
		return ret

s = Solution()
print (s.twosum([-1, 2, 3, 1,-3,-4,7,5,6,-2], 0))

		