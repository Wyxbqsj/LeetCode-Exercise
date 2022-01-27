from typing import List
'''
f[0][j]=1
f[i][numRows-1]=1
f[i][j]=f[i-1][j-1]+f[i-1][j]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        f=[]
        for x in range(numRows):
            dp=[1 for _ in range(x+1)]
            f.append(dp)
        
        for i in range(2,numRows):
            for j in range(i+1):
                if j!=0 and j!=i:
                    f[i][j]=f[i-1][j-1]+f[i-1][j]
        return f

                
            
            
            
            
        