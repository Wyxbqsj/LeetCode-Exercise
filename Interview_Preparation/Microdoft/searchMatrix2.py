# 时间复杂度为O(m+n)的方法：从左下角逼近到右上角，也可以是右上角逼近左下角
# 如果是左上角逼近右下角的话，当前的matrix[i][j]是第i行的最小值，第j列最小值，当它比target大或小根本不能只移动一个参数，因此又会回到双重循环当中
class Solution:
    def searchMatrix(self, matrix, target):  
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        m,n=len(matrix),len(matrix[0])
        i=m-1
        j=0
        count=0
        # 注意matrix是行和列都排序好了的矩阵
        while i>=0 and j<n:
            if matrix[i][j]<target: # 如果当前数据比target小，则在当前行往后搜索
                j+=1
            elif matrix[i][j]>target: # 如果当前数据比target大，则整行都不满足，直接去上一行搜索
                i-=1
            else: # 若当前数据等于target，则向右上角走一步
                count+=1
                i-=1
                j+=1
        return count
        
            
            