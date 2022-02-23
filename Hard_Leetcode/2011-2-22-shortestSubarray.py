import collections
from typing import List
# 题目：https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/
'''
1.首先计算原数组前缀和，用于快速计算区间[i，j]的子数组和。
2.枚举每个前缀，维护到一个单调递增的双端队列中。
3.对比当前前缀和与双端队列的第一个元素（最小元素），通过差值算出区间和是否达到k，如果达到k则将区间长度添加到答案中。
3.弹出第一个元素，继续对比第二元素，缩短区间寻找更优解。
'''
# 注意：单端队列只有popleft()操作
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # 建立前缀和数组，preSum[i]=nums[0]+...+nums[i-1]
        preSum=[0]
        for x in nums:
            preSum.append(preSum[-1]+x)
        
        ans=float('inf') # 最短的非空子数组的长度先初始化为无穷大
        
        # 构造单调队列q
        q=collections.deque() # q中元素格式：(i,preSum[i])
        for i,sum_i in enumerate(preSum):
            while q and sum_i<q[-1][1]: # 当前值sum_i比队列末尾的值小时，将末尾的值pop()出来，来保持q的递增性质
                q.pop()
            
            while q and sum_i-q[0][1]>=k: # 每次遇到符合条件的，那肯定比较的是队列中的第一个数与最后一个数的差值
                # 若符合，就把第一个数扔掉，每次都记录下最短的非空子数组
                ans=min(ans,i-q.popleft()[0]) # q.popleft()取q中第一个值，[0]表示取索引
            
            q.append((i,sum_i))
        
        return ans if ans!=float('inf') else -1
        
# 构造一个单调队列q的基本操作：
'''
q=collections.deque()
for i in nums:
    while q and i<q[-1]:
        q.pop()
    q.append(i)         
'''           

# 构造一个单调栈的基本操作：
'''
l=[]
for i in nums:
    while l and i<l[-1]:
        l.pop()
    l.append(i)
'''           
            
            