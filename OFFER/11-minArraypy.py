# 题目：剑指 Offer 11. 旋转数组的最小数字，https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
class Solution:
    def minArray(self,numbers):
        # 二分法找分割点，对于最小点那个位置，它之前的数都比数组最后一位数大，之后的数都比数组最后一位小
        n=len(numbers)
        left,right=0,n-1
        while left<right:
            mid=(left+right)//2
            if numbers[mid]>numbers[right]:
                left=mid+1
            elif numbers[mid]<numbers[right]:
                right=mid
            else: # 注意有重复元素，每次得到numbers[mid]==numbers[right]时，去重，right左移
                right-=1
        return numbers[right]
        
