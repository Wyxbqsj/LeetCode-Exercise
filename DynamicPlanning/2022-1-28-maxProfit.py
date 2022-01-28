from typing import List
# 第i天买入，第j天卖出所得到的利润为f[i][j]
# 当j<=i都为0
# f[i][j]=prices[j]-prices[i]
# 这是暴力搜索，双层循环，不是DP，超过了时间限制
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        maxP=0                       
        for i in range(length):
            for j in range(length):
                tmp=prices[j]-prices[i]
                if j>i and tmp>0 and tmp>maxP:
                    maxP=tmp
        return maxP
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 最优策略的最后一步：在第x天卖出股票获得了最大收益
        # 子问题：在前x天的某一天买入，在x天卖出获得了最大收益
        # f[x]表示在前x天卖出获得的最大利益
        # f[x]=max{f[x-1], prices[x]-min(prices[:x-1])}
        length=len(prices)
        f=[0 for _ in range(length)]
        f[0]=0 # 因为不能当天买卖，所以第一天买第一天卖收益是0
        minP=prices[0]
        maxP=0
        for i in range(1,length):
            # tmp=min(prices[:i]) # 记录前i天最低的价格，不可以直接调用min函数（O(N)的复杂度）
            minP=min(minP,prices[i])
            f[i]=max(f[i-1],prices[i]-minP)
            maxP=max(f[i],maxP)
        return maxP
x=Solution()
a=x.maxProfit([1,2])
print(a)
        