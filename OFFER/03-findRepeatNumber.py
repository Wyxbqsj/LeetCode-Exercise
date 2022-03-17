# 题目：剑指 Offer 03. 数组中重复的数字，https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
'''
方法一：哈希表,时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def findRepeatNumber(self,nums):
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for k in dic.keys():
            if dic[k]>=2:
                return dic[k]
        return -1
'''

'''
方法二：先排序，然后看看相邻元素是否相同，时间复杂度O(nlogn)，空间复杂度O(1)
class Solution:
    def findRepeatNumber(self,nums):
        nums.sort()
        n=len(nums)
        if n<=1:
            return -1
        pre=nums[0]
        for i in range(1,n):
            if nums[i]==pre:
                return 
            else:
                pre=nums[i]
        return -1
'''

'''
方法三：原地哈希，不用到字典，由于题目中指出，nums当中的数都在0到n-1的范围内
因此将数字nums[i]放到索引为nums[i]这个位置
遍历数组，发现位置i处不是i时，将nums[i]交换到索引为nums[i]的位置，交换之前先判断一下，若该位置的元素已经等于nums[i]了，那就说明重复了，则return
例如nums=[2,1,5,0]，遍历数组后，按照上述规则修改后，nums=[0,1,2,null,null,5]
时间复杂度O(n)，空间复杂度O(1)
'''
class Solution:
    def findRepeatNumber(self,nums):
        for i in range(len(nums)):
            while i!=nums[i]:
                tmp=nums[i]
                if nums[i]==nums[tmp]:
                    return nums[i]
                nums[tmp],nums[i]=nums[i],nums[tmp]
        return -1
x=Solution()
a=x.findRepeatNumber([1,1])
print(a)
            