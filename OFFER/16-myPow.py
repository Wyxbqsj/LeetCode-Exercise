# 题目：剑指 Offer 16. 数值的整数次方，https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/

'''方法一：暴力解，会越界
class Solution:
    def myPow(self,x,n):
        if n==0:
            return 1
        res=1
        if n<0:
            x=1/x
            n=-n
        for i in range(n):
            res*=x           
        return res 
'''

# 方法二：快速幂，解析过程：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/
# 快速幂的思想就是：比如求x^11，正常乘积需要循环乘11次，时间复杂度为O(n)
# 快速幂将指数11转成了二进制数1011，那么原来的式子x^11=x^(2^3+2^1+2^0)=x^(2^3)*x^(2^1)*x^(2^0)，只需要乘3次，复杂度降到O(logn)
class Solution:
    def myPow(self,x,n):
        if x==0: # 避免下面x=1/x报错
            return 0
        if n<0:
            x,n=1/x,-n
        res=1
        while n:
            if n&1: # n的二进制位最后一位若是1，则需要乘一次
                res*=x
            n//=2 # 二进制位往前进一位，即丢掉最后一位
            x*=x # 同时x需要变大一倍，因为我们每次累乘的是x的次幂，而非乘一个x
            
        return res 