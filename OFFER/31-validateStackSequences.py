# 题目：剑指 Offer 31. 栈的压入、弹出序列，https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
# 借用辅助栈，模拟栈的压入和弹出过程
# 入栈操作：按照压栈序列pushed的顺序执行
# 出栈操作：每次入栈后，循环判断“栈顶元素==popped序列的当前元素”是否成立，若符合，则将满足要求的栈顶元素全部弹出
class Solution:
    def validateStackSequences(self,pushed,poped):
        stack=[]
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]==poped[0]:
                stack.pop()
                poped.pop(0)

        if not stack:
            return True
        return False
        