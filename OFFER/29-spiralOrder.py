# 题目：剑指 Offer 29. 顺时针打印矩阵，https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m,n=len(matrix),len(matrix[0])
        res=[]
        visited=[[0]*n for _ in range(m)]
        i,length=0,m*n
        directions=[[0,1],[1,0],[0,-1],[-1,0]] # 向右、向下、向左、向上四个方向
        x,y=0,-1 # 由于第一步往右走，所以y的初始值为-1
        while i<length:
            for d in range(4):
                # 注意一定要先走一步，所以初始的x,y不能为0，0，不然跳出下面的while循环后visited[x][y]一直得到的是访问过的状态，会进入死循环
                x=x+directions[d][0]
                y=y+directions[d][1]
                while 0<=x<m and 0<=y<n and visited[x][y]==0:
                    res.append(matrix[x][y])
                    i+=1
                    visited[x][y]=1
                    x=x+directions[d][0]
                    y=y+directions[d][1]
                x=x-directions[d][0]
                y=y-directions[d][1]
        return res
                
                
            
            
        
        