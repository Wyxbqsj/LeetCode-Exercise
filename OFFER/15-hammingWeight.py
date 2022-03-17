# 题目：剑指 Offer 15. 二进制中1的个数，https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
# 注意题目已经指出，输入必须是长度为32的二进制串
class Solution:
    def hanmingWeight(self,n):
        count=0
        while n:
            if n&1==1:
                count+=1
            n=n//2
        return count
                
            