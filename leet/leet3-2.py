class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) <= 2:
            return []

        ret = []
        tar = 0
        num.sort()
        i = 0
        while i < len(num) - 2:
            if i != 0 and num[i] == num[i-1]:
                i += 1
                continue
            j = i + 1
            k = len(num) - 1
            while j < k:
                if num[i] + num[j] + num[k] < tar:
                    j += 1
                elif num[i] + num[j] + num[k] > tar:
                    k -= 1
                else:
                    ret.append([num[i], num[j], num[k]])
                    j += 1
                    k -= 1
                    # folowing 3 while can avoid the duplications
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                    while j < k and num[k] == num[k + 1]:
                        k -= 1
            i += 1
        return ret

# debug

s = Solution()
print (s.threeSum([1, -1, 0,-1,-3, -2, 2]))
print (s.threeSum([-1,0,1,2,-1,-4, -1, -1, -2, -3, -4]))
