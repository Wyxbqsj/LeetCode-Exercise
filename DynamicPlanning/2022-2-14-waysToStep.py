class Solution:
    def waysToStep(self, n: int) -> int:
        # f[x]=f[x-1]+f[x-2]+f[x-3]

        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 4
        p,q,r=1,2,4
        for i in range(3,n):
            s=p+q+r
            p,q,r=q,r,s
        return s%1000000007               
            