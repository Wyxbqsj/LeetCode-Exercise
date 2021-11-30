'''
自动机：（确定有限状态机DFA）
我们的程序在每个时刻有一个状态 s，每次从序列中输入一个字符 c，并根据字符 c 转移到下一个状态 s'。
这样，我们只需要建立一个覆盖所有情况的从 s 与 c 映射到 s' 的表格即可解决题目中的问题。
'''
INT_MAX=2**31-1
INT_MIN=-2**31

class Automation:
    def __init__(self):
        self.state='start'
        self.sign=1
        self.ans=0
        self.table={ #程序有4种状态
            'start': ['start','signed','in_number','end'], #状态为start时，若读取的下一个字符是' '，则状态仍为start；读取字符为'+/-'，状态为signed;读取字符为number，状态为in_number；读取的是其他字符，则状态为end
            'signed':['end','end','in_number','end'],
            'in_number':['end','end','in_number','end'],
            'end':['end','end','end','end'],
        }
    
    def get_col(self,c):
        if c.isspace():
            return 0
        if c=='+' or c=='-':
            return 1
        if c.isdigit():
            return 2
        return 3
    
    def get(self,c):
        self.state=self.table[self.state][self.get_col(c)]
        if self.state=='in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state=='signed':
            self.sign=1 if c=='+' else -1
            

class Solution:
    def myAtoi(self, str:str)->int:
        automation=Automation()
        for c in str:
            automation.get(c)
        return automation.sign*automation.ans


x=Solution()
a=x.myAtoi("-+42")    
print(a)  