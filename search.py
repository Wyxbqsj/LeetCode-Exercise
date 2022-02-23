from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(right+left)//2 # 第一次二分找分割点，该位置之前的元素都比数组的第一个元素nums[0]大，之后都比nums[0]小
            if nums[mid]>=nums[0]: # 表明mid之前的元素都比nums[0]大，则最小值肯定不在里面，因此左边界右移
                left=mid+1
            else: # 表明mid之后的元素都比nums[0]小，但这些元素保持一个递增关系，则最小值肯定在mid之前或者就是mid，因此右边界左移
                right=mid
        
        def bisearch(a,start,end,t):
            while start<end:
                mid=(start+end)//2
                if a[mid]>=t:
                    end=mid
                else:
                    start=mid+1
            return end
        
        if nums[-1]>=nums[0]: # 因为line25在前半部分有序区间[0,right-1]内找target，若上面求出right=len(nums)-1，但是整个数组都是有序的，则后面变成了在(0,len(nums)-2)里面找，就会少了最后一个元素
            right=len(nums)
        
        if target>nums[0]:
            res=bisearch(nums,0,right-1,target)
        else:
            res=bisearch(nums,right,len(nums)-1,target)
        
        return res if nums[res]==target else -1

x=Solution()
a=x.search([1,2,3,4,5],5)
print(a)