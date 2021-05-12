'''
题目：给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
'''

#我的思路：暴力枚举，返回使得差值最小的那个三数之和。在leetcode上跑出来的结果是错的，可能是因为超出了时间限制
'''
class Solution:
    def threeSumCloset(self, nums, target):
        nums.sort()
        minimun=100000
        for first in range(len(nums)):
            for second in range(first+1,len(nums)):
                for third in range(second+1,len(nums)):
                    ans=nums[first]+nums[second]+nums[third]
                    if abs(ans-target)<minimun:
                        minimun=abs(ans-target)            
        return ans
'''

#看题解后：（对枚举的过程进行优化）
'''
先枚举a，它在数组中的位置为i
用pb和pc分别表示指向b和c的指针，初始时，pb指向位置i+1，即左边界；pc指向len(nums)-1，即右边界。
在每一步枚举的过程中，用a+b+c来更新答案，并且，如果
1）如果a+b+c>target，就将pc向左移动一个位置（和大了，要让它变小点）
2）如果a+b+c<target，就将pb向右移动一个位置（和小了，要让它变小点）
'''
class Solution:
    def threeSumCloset(self, nums, target):
        nums.sort()
        best=10000000

        #根据绝对值的差值来更新答案
        def update(x):
            nonlocal best 
            '''非局部声明变量指代的已有标识符是最近外面函数的已声明变量，但是不包括全局变量。
            这个是很重要的，因为绑定的默认行为是首先搜索本地命名空间。nonlocal声明的变量只对局部起作用，离开封装函数，那么该变量就无效。
            比如这里的best就定义在函数threeSumCloset内，若best是全局变量，定义在类内，但在函数threeSumCloset外，则nonlocal报错
            '''
            if abs(x-target)<abs(best-target):
                best=x

            
        for pa in range(len(nums)):
            if pa>0 and nums[pa]==nums[pa-1]:
                continue
            pb,pc=pa+1,len(nums)-1
            while pb<pc:
                ans=nums[pa]+nums[pb]+nums[pc]
                if ans==target:
                    return target
                update(ans) #要对ans进行更新，否则一直是第一次计算的值
                if ans>target:
                    pc0=pc-1
                    while pb<pc0 and nums[pc0]==nums[pc]: #剔除重复元素，后一个数不能和前面的数相同
                        pc0=pc0-1
                    pc=pc0
                else:
                    pb0=pb+1
                    while pb0<pc and nums[pb0]==nums[pb]: #剔除重复元素，后一个数不能和前面的数相同
                        pb0=pb0+1
                    pb=pb0 
                    #像这种i=i+1的迭代，要放在循环里才行，不然他只会执行一次呀
        return best
x=Solution()
a=x.threeSumCloset([1,1,1,0], -100)
print (a)



