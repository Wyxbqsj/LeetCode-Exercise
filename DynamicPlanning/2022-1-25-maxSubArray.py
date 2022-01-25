from typing import List

'''
分析过程：假设最大和是sum
1、确定状态：
（1）最后一步：最后一个加入的数字是nums[i-1]
（2）子问题：在nums数组中找出以第i个数结尾的最大连续子数组和
2、转移方程：f[x]=以第x个数结尾的连续子数组的最大和
f[x]=max(f[x-1]+nums[x-1],nums[x-1])
3、初始条件和边界情况：
（1）初始条件：f[1]=nums[0]
（2）边界情况：x<=n-1
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length=len(nums)
        memo=[-99999 for _ in range(length+1)] # 初始化数组f[]，下标从1开始
        memo[1]=nums[0] # 初始条件：以第1个数结尾的连续子数组的最大和就是nums[0]
        i=2    
        while i<=length: # 边界条件：数组不要越界
            memo[i]=max(memo[i-1]+nums[i-1],nums[i-1])
            i+=1
        return max(memo) # 将所有可能性记录在了memo中，最后返回其中的最大值

# 改进，最后在整个memo中找最大值，有些过于复杂了，可以直接在建立memo的时候，边建立边找最大值
'''
考虑到 f(i)只和 f(i-1)相关，于是我们可以只用一个变量pre来维护对于当前f(i)的 f(i-1)的值是多少，从而让空间复杂度降低到O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length=len(nums)
        memo=[-99999 for _ in range(length+1)] 
        memo[1]=nums[0] 
        i=2  
        while i<=length: 
            memo[i]=max(memo[i-1]+nums[i-1],nums[i-1])
            res=max(memo[i],res)
            i+=1
        return res
似乎时间更久内，官方更简洁的答案：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre=0
        maxsum=nums[0]
        for i in range(len(nums)):
            pre=max(pre+nums[i],nums[i])
            maxsum=max(pre,maxsum)
        return maxsum
'''