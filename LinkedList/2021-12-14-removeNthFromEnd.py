# Definition for singly-linked list.
from typing import List

# 栈方法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 遍历链表，将链表中的结点依次入栈，最后弹出第n个结点即可
        dummy=ListNode(0,head)
        stack=[] # 定义栈 也可写成stack=list()
        cur=dummy # 在栈的尾部也就是链表的起点加一个dummy node，就不用担心访问到头结点了
        while cur:
            stack.append(cur)
            cur=cur.next
        
        for i in range(n): # 将要栈中要删除的鹅结点的前面的结点全部删除，即为了找到待删除的结点的前驱结点
            stack.pop()
        
        # 以上操作对原链表无任何影响，只是在head前添加了一个dummy node
        # 比如当head=[1],n=1
        # pre=dummy
        # pre.next=head
        # pre.next.next=None
        pre=stack[-1] # 待删除的节点的前驱结点
        pre.next=pre.next.next 
        return dummy.next
        
            
        