# 题目：剑指 Offer 10- II. 青蛙跳台阶问题，https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
# 动态规划
class Solution:
    def numWays(self,n):
        # f[x]=f[x-1]+f[x-2]
        if n<=1:
            return 1
        dp=[0 for _ in range(n+1)]
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]%1000000007