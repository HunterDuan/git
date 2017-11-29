#查找给定数字是否存在二维数组中
class Solution:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        m = len(array) - 1  #列表没有shape属性
        i = 0

        while m >= 0 and i < len(array[0]): 
            if array[m][i] > target:
                m -= 1
            elif array[m][i] < target:
                i += 1
            else:
                return 1
        return 0
#debug
s = Solution()
s.Find([[1,2,3],[3,4,5],[4,5,6]],6)