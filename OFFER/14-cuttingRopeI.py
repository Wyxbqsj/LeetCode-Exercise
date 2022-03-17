# 题目：剑指 Offer 14- I. 剪绳子，https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
'''方法一：动态规划，时间复杂度O(n^2)，空间复杂度O(n)
class Solution:
    def cuttingRope(self,n):
        # dp[i]表示长度为i的绳子剪成m段后的最大乘积，注意m>=2
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(3,n+1):
            for j in range(2,i): # 绳子的总长度是i，第一次可以剪j长度，若j=1，对最后乘积没有帮助，因此j从2出发
                # 若剩下的i-j长度不再剪，则乘积为i*(i-j)；
                # 如果剩下的i-j继续剪，则乘积为当前剪下的一段长度j乘上“长度为i-j的绳子的最大乘积”，即j*dp[i-j]
                tmp=max(j*(i-j),j*dp[i-j]) 
                # 我们尝试所有的j并让dp[i]等于最大的那个值
                dp[i]=max(tmp,dp[i])
        return dp[n]
'''           

# 方法二：贪心法+数论，核心思路是：尽可能把绳子分成长度为3的小段，这样乘积最大. 时间复杂度O(n)，空间复杂度O(1)
# 证明过程：
# 1. 任何大于1的数都可以由2和3组成（根据奇偶证明）
# 2. 因为2*2=1*4，2*3>1*5，所以将数字拆成2和3得到的乘积最大
# 3. 又因为2*2*2<3*3，所以3越多乘积越大
class Solution:
    def cuttingRope(self,n):
        if n==1:
            return 0
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
        return res*n
        
