from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        # f[x]表示数x的二进制表示中1的个数
        # 如果x是偶数，则f[x]=f[x/2];
        # 如果x是奇数，则f[x]=f[x-1]+1
        # 1、如果 i 为偶数，那么f(i) = f(i/2) ,因为 i/2 本质上是i的二进制左移一位，低位补零，所以1的数量不变。
        # 2、如果 i 为奇数，那么f(i) = f(i - 1) + 1， 因为如果i为奇数，那么 i - 1必定为偶数，而偶数的二进制最低位一定是0，
        # 那么该偶数 +1 后最低位变为1且不会进位，所以奇数比它上一个偶数bit上多一个1，即 f(i) = f(i - 1) + 1。
        dp=[0]
        for i in range(1,n+1):
            if i%2==0:
                dp.append(dp[i//2]) # 注意一定要用i//2取整，i/2得到的是float型数据
            else:
                dp.append(dp[i-1]+1)
        return dp

x=Solution()
a=x.countBits(2)
print(a)