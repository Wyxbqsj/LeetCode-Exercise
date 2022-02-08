from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # “可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。”
        # 这句话是为了确定初始值，即f[0]=f[1]=0
        # 因此动态转移方程只有一个，即：f[x]=min(f[x-1]+cost[x-1],f[x-2]+cost[x-2])
        length=len(cost)
        f=[0 for _ in range(length+1)]
        f[0]=f[1]=0
        for i in range(2,length+1):
            f[i]=min(f[i-1]+cost[i-1],f[i-2]+cost[i-2])
        return f[length]