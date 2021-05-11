'''
题目：
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
'''

'''我的思路，失败！会造成无止尽的嵌套循环判断
class Solution:
    def threeSum(self,nums):
        def out(L,a,b,c):
            abc=[]
            ia=L.index(a)
            ib=L.index(b)
            ic=L.index(c)
            iL=[ia,ib,ic]
            iL.sort()
            for i in iL:
                abc.append(L[i])
            return abc
        if len(nums)<3:
            res=[]
        else:
            res=[]
            pnums=[x>=0 for x in nums]
            nnums=[x<0 for x in nums]
            pnums.sort()
            nnums.sort(reverse=True)
            i=0
            if len(pnums)<=len(nnums):
                while i<len(pnums):
                    j=0
                    while j<len(nnums):
                        if pnums[i]+nnums[j]<0:
                            ans=pnums[i]+nnums[j]+pnums[i+1]
                            if ans==0:
                                res.append(out(pnums[i],nnums[j],pnums[i+1]))
                            if ans>0:
'''
#看题解后：使用双指针——当我们需要枚举数组中的两个元素时，如果我们发现随着第一个元素的递增，第二个元素是递减的，那么就可以使用双指针的方法，将枚举的时间复杂度从O(n2)降至O(n)
class Solution():
    def threeSum(self,nums):
        nums.sort()
        res=list() #!!!注意是这样生成一个空的二维list,再可以直接append
        if len(nums)<3:
            return []
        else:
            #first和Second都属于第一类指针：从前往后（递增）
            #third是第二类指针，从后往前（递减）
            first=0
            for first in range(len(nums)):
                if first>0 and nums[first]==nums[first-1]:#剔除重复元素
                    continue
                third=len(nums)-1
                for second in range(first+1,len(nums)):
                    if second>first+1 and nums[second]==nums[second-1]:#剔除重复元素
                        continue
                    while second<third and nums[first]+nums[second]+nums[third]>0:
                        third=third-1 #三个数之和大于0，要把最大的数，也就是nums[third]减小一点
                    if second==third:
                        break
                    if nums[first]+nums[second]+nums[third]==0:
                        res.append([nums[first],nums[second],nums[third]]) #直接append上一个list
            return res

x=Solution()
a=x.threeSum([])
print(a)
                            
                    