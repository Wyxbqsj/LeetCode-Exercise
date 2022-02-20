from itertools import count


class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if len(matrix)==0 or len(matrix[0])==0: # 判断一个矩阵为空的正确方式
            return 0
        
        count=0
        m=len(matrix)
        n=len(matrix[0])
        i=0
        # 是剪枝后的O(m*n)时间复杂度，因为仍然有两层循环
        while i<m:
            if matrix[i][0]==target:
                count+=1
                
            else:
                j=1
                while j<n:
                    if matrix[i][j]==target:
                        count+=1
                        break
                    elif matrix[i][j]>target:
                        break
                    else:
                        j+=1
            i+=1
        return count
       
                    