# Definition for singly-linked list.
# 方法一：将中间要反转得部分截取下来，然后反转后再接回去
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head.next or left==right:
            return head
        def reverse(h):
            pre=None
            cur=h
            while cur:
                post=cur.next 
                cur.next=pre
                pre=cur
                cur=post 
            return pre
        
        dummy=ListNode(0,head)
        count=0
        curr=dummy
        while curr and count<right:
            if count==left-1:
                before=curr
                newHead=curr.next
            count+=1
            curr=curr.next
       
        after=curr.next
        curr.next=None
        newHead=reverse(newHead)
        last=newHead
        while last.next:
            last=last.next 
        before.next=newHead
        last.next=after # 修改节点当中的next才能修改这个节点指向的下一个节点。last=after只是把after赋值给last,并没有修改指向
        return head
                
                
                