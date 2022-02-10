class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1
        T=[0 for i in range(n+1)]
        T[1]=1
        T[2]=1
        for i in range(3,n+1):
            T[i]=T[i-3]+T[i-2]+T[i-1]
        return T[n]
    
    # 上面时时间复杂度和空间复杂度都是 O(n)O(n) 的实现；
    # 由于 T(n)只和前三项有关，因此可以使用「滚动数组思想」将空间复杂度优化成 O(1)
    '''
    p,q,r=0,1,1 # 初始化T0,T1,T2
    for i in range(3,n+1):
        s=p+q+r # 当前Ti的值
        p,q,r=q,r,s # 往后递推一位，记录接下来三个数即可
    '''