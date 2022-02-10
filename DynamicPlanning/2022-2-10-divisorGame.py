class Solution:
    def divisorGame(self, n: int) -> bool:
        '''
        注意A和B都采用最优策略：
        1. 如果N是奇数，因为奇数的所有因数都是奇数，因此 N 进行一次 N-x 的操作结果一定是偶数，所以如果 a 拿到了一个奇数，那么轮到 b 的时候，b拿到的肯定是偶数，这个时候 b 只要进行 -1， 还给 a 一个奇数，那么这样子b就会一直拿到偶数，到最后b一定会拿到最小偶数2，a就输了。
        2. 所以如果游戏开始时Alice拿到N为奇数，那么她必输，也就是false。如果拿到N为偶数，她只用 -1，让bob 拿到奇数，最后bob必输，结果就是true。
        因此代码可以为：
        if n%2==0: return True
        else: return False
        '''
        
        '''
        动态规划：
        1. 将所有的<=N 的解都找出来，基于前面的，递推后面的。
        2. 状态转移: 如果 i 的约数里面有存在为 False 的（即输掉的情况），则当前 i 应为 True；如果没有，则为 False。
        '''
        if n<=1:
            return False
        dp=[False for _ in range(n+1)]
        dp[1]=False # Alice最后抽到1，则她失败
        dp[2]=True # Alice最后抽到2，则她获胜
        for i in range(3,n+1): # 所有可能的"n"
            for x in range(1,i//2): # 注意玩家都是以最佳状态参与游戏，第二个循环表示，当n==i时，x可取的范围，取一半即可
                if i%x==0 and dp[i-x]==False: # 若存在当前选择的x满足要求，即n%x==0,且下一步n=n-x时对方必败，则A胜利
                    dp[i]=True
                    break
        return dp[n]
            

