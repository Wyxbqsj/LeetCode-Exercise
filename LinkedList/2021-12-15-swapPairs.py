# Definition for singly-linked list.
# 用栈做辅助来存储
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        stack=[]
        dummy=ListNode(0)
        pre=dummy # pre用来控制新链表的生成
        cur=head
        while cur: # cur用来遍历原链表
            stack.append(cur.val)
            cur=cur.next
            if len(stack)==2: # 每次压入栈中两个node，再pop()出来
                while stack:
                    pre.next=ListNode(stack.pop())
                    pre=pre.next
        if stack:
            pre.next=ListNode(stack.pop())
        return dummy.next
            
            