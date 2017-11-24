class Solution:
    def atoi(self,strg=None):
        if not isinstance(strg,str):
            return 0
        elif len(strg.strip()) == 0:
            return 0
        else:
            self.strg = strg.strip()
        Max_int = 2147483647
        Min_int = -2147483648
        sign = 1
        fir = 0
        The_int = 0
        
        if strg[fir] == '-':
            fir += 1
            sign = -1
        elif strg[fir] == '+':
            fir += 1

        for i in range(fir,len(strg)):
            if not strg[i].isdigit():
                break
            The_int = The_int * 10 + int(strg[i])#返回整数
        if Min_int <= The_int <= Max_int:
            return sign*The_int
        else:
            return  Max_int if sign == 1 else Min_int
#debug
s = Solution()
print (s.atoi())
