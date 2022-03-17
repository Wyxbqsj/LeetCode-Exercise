# 题目：剑指 Offer 14- II. 剪绳子 II，https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
# 与剪绳子I不同的是n的取值范围，2<=n<=1000
class Solution:
    def cuttingRope(self,n):
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        res=1
        while n>4:
            res*=3
            n-=3
        return res*n%1000000007