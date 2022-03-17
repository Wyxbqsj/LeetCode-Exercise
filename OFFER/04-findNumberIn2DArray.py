# 题目：剑指 Offer 04. 二维数组中的查找，https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
# 根据matrix的递增性质，从左下角往右上角逼近
class Solution:
    def findNumberIn2DArray(self,matrix,target):
        if not matrix or not matrix[0]:
            return False
        m=len(matrix)
        n=len(matrix[0])
        i,j=m-1,0
        while i>=0 and j<n:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                i-=1
            else:
                j+=1
        return False