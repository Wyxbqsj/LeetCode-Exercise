class Solution:
    def fib(self, n: int) -> int:
        if n<=1: # 注意一定要有这个边界判断，否则当n=0时，dp[1]是没有意义的，无法赋值
            return n
        dp=[0 for _ in range(n+1)]
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]