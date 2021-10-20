class Solution:
    #用动态规划的办法找出所有回文串，再找出长度最大的那个
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        dp=[[False]*n for x in range(n)] #记录P(i,j)的结果，初始化都为False
        for i in range(n):
            dp[i][i]=True
        max_len=1
        begin=0
        #先枚举字串长度，巧妙的地方！没有用双指针来控制字符串首尾，明显无法控制
        for length in range(2,n+1):
            for i in range(n): # i是左边界，j-i+1=length
                j=length+i-1
                if j>=n: # 注意等于号，右边界一越界，立刻终止
                    break
                if s[i]!=s[j]:
                    dp[i][j]=False
                else:
                    if j-i<3: #如果子串长度等于1或者2，首尾两字母又相等，则dp[i][j]一定为真
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                
                if dp[i][j] and j-i+1>max_len:
                    max_len=j-i+1
                    begin=i
        return s[begin:begin+max_len]

x=Solution()
a=x.longestPalindrome("cbbd")
print(a)