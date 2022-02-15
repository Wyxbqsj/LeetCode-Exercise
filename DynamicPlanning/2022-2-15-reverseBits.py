'''
题目：翻转数位
给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
'''
class Solution:
    def reverseBits(self, num: int) -> int:
        before=0 # 记录从尾部开始当前，连续1的个数
        after=0 # 将一个数位从0变为1后连续1的个数
        res=0 # 最终的最长的一串1的长度
        for i in range(32): # 题目已经说明是32位，无需在求出num转成2进制后的实际长度，不足32位的前面都补0即可
            if (num&1)==1: # 判断num转成2进制后最后一位是不是1，若是1
                before+=1 
                after+=1
            else: # 若是0
                after=before+1 # 逆转一位0，after记录该0位之前1的串的长度，再加上当前这个1
                before=0 # 发现0后，重新记录连续的1，因词before又从0开始
            res=max(res,after) # 结果是after中的最大值
            num=num//2 # num的二进制位向右移动一位
        return res

a=Solution()
x=a.reverseBits(3)
print(x)
                