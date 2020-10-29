'''
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
子数组 定义为原数组中的一个连续子序列。
请你返回 arr 中 所有奇数长度子数组的和 。
'''

class Solution:
    def sumOddLengthSubarrays(self, arr):
        total=0
        for footstep in range(1,len(arr)+1,2):
            for i in range(0,len(arr)-footstep+1): #步长
                total=total+sum(arr[i:i+footstep])  #i+footstep<len(arr)+1(注意！range(x,y)生成的是[x,y)这样半开半闭的区间，所以最后要有+1)
        return total

            
x=Solution()
a=x.sumOddLengthSubarrays([10,11,12])  
print(a)        
            

