# 题目：剑指 Offer 21. 调整数组顺序使奇数位于偶数前面，https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
# 使得数组nums奇数在前，偶数在后
from typing import List

class Solution:
    def exchange(self,nums:List[int]):
        l,r=0,len(nums)-1
        while l<r:
            while l<r and nums[l]&1:
                l+=1
            while l<r and nums[r]&1==0:
                r-=1
            nums[l],nums[r]=nums[r],nums[l]
        return nums
x=Solution()
a=x.exchange([])
print(a)
            