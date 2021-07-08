#给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#解决思路：动态规划
'''
我们用 f(i)f(i) 代表以第 ii 个数结尾的「连续子数组的最大和」，那么很显然我们要求的答案就是max{f(i)}
因此我们只需要求出每个位置的 f(i)，然后返回f数组中的最大值即可。
如何求 f(i): 我们可以考虑 nums[i]单独成为一段还是加入f(i−1)对应的那一段，
这取决于nums[i]和f(i-1)+nums[i]的大小，我们希望获得一个比较大的，于是可以写出这样的动态规划转移方程：
f(i)=max{f(i-1)+nums[i],nums[i]}
'''
class Solution:
    def maxSubArray(self, nums):
        pre=0
        maxsum=nums[0]
        for i in range(len(nums)):
            pre=max(pre+nums[i],nums[i])
            maxsum=max(pre,maxsum)
        return maxsum

x=Solution()
a=x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(a)
                

