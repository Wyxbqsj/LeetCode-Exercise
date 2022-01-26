'''
最后一步：爬a个台阶（a=1 or 2）
子问题：每次爬1或2个台阶，需要n-a阶到达当前n-a台阶,有多少种方法
转移方程：f[x]=有多少种方法到达当前x台阶
f[x]=f[x-1]+f[x-2]*2
初始条件：f[1]=0, f[2]=2
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: # 不要忘记考虑边界条件，当n=1时，按照如下方式定义的f[]只有f[0]和f[1]，直接赋值f[2]会报错
            return n
        f=[0 for _ in range(n+1)]
        f[1]=1
        f[2]=2
        i=3
        for i in range(3,n+1):
            f[i]=f[i-1]+f[i-2]
        return f[n]
            