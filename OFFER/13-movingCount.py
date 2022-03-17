# 剑指 Offer 13. 机器人的运动范围，https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
# 深度遍历：将不满足条件的数剃掉，计数即可
class Solution:
    def movingCount(self,m,n,k):
        def judge(x,y):
            ans=0
            while x or y:
                if x:
                    ans+=x%10
                    x//=10
                if y:
                    ans+=y%10
                    y//=10
            return True if ans<=k else False
        
        dx,dy=[1,-1,0,0],[0,0,1,-1]
        self.res=0
        visited=[[False]*n for _ in range(m)]
        def dfs(x,y):
            # 递归出口：
            if not 0<=x<m or not 0<=y<n: # 越界
                return # 只是修改self.res的值，所以直接return即可
            if not judge(x,y) or visited[x][y]: # 横纵坐标数位和不满足要求，或者当前坐标已被访问过
                return
            visited[x][y]=True
            self.res+=1
            for t in range(4):
                i,j=x+dx[t],y+dy[t]
                dfs(i,j)
        
        if k==0:
            return 1
        dfs(0,0)
        return self.res
        
                
            
            