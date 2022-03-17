# 题目：剑指 Offer 30. 包含min函数的栈，https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/


class MinStack:
    def __init__(self) -> None:
        self.A=[]
        self.B=[]
        
    def push(self,x):
        self.A.append(x)
        # B是一个单调栈，用来保证B中的元素是递增的（可以有相等元素），B的栈顶源素即为最小值
        if not self.B or self.B[-1]>=x:
            self.B.append(x)
    
    def pop(self):
        if self.A[-1]==self.B[-1]:
            self.B=self.B[:-1]
        self.A=self.A[:-1]
    
    def top(self):
        return self.A[-1]
    
    def min(self):
        return self.B[-1]
        