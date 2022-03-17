# 题目：剑指 Offer 09. 用两个栈实现队列，https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
# 一个队列的两个功能分别用两个栈来实现，栈1实现入队功能，栈2实现出队功能
# 思路：栈：先进后出；队列：先进先出；因此可以利用两个栈实现倒序
# 将栈1中的元素全部pop()到栈2中即实现了逆序，此时再删除栈2的栈顶元素即实现了队列的出队功能


class CQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    
    def appendTail(self,value):
        self.stack1.append(value)
    
    def deleteHead(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return -1 if not self.stack2 else self.stack2.pop()

x=CQueue()
x.appendTail(3)
param_2=x.deleteHead()
print(param_2)