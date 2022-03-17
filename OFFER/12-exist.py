# 题目：剑指 Offer 12. 矩阵中的路径，https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/


class Solution:
    def exist(self,board,word):       
        def DFS(x,y,k): # 传入当前起点，以及等待比较的word中的字符
            # 递归出口
            if (x<0 or x>=m) or (y<0 or y>=n) or board[x][y]!=word[k]: # 若x或y越界，或者当前遍历的字符与word中字符不匹配，则返回False
                return False
            if k==len(word)-1: # 若已经判断到最后一个字符都相同，则返回True
                return True
            
            tmp=board[x][y] # 记录当前遍历的字符
            board[x][y]=None # 将遍历过的位置记为空
            res=DFS(x+1,y,k+1) or DFS(x-1,y,k+1) or DFS(x,y+1,k+1) or DFS(x,y-1,k+1) # 向四个方向深度遍历，匹配下一个字符，因为到了这一步说明board[x][y]=word[k]，因此我们比较下一个数
            board[x][y]=tmp # 还原刚刚遍历过的那个字符，因为一条路走不通，会返回到上一步，走下一条
            return res
        
        if not board or not board[0]: # 判断一下矩阵是否为空
            return False
        m,n=len(board),len(board[0])
        # 以矩阵board的每个位置作为起点，判断是否有路径
        for i in range(m): 
            for j in range(n):
                if DFS(i,j,0): return True # 只要有一条，就返回True
        # 都找不到，则返回False
        return False
        
            
                