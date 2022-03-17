# 题目：剑指 Offer 18. 删除链表的节点，https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.next=None
        self.val=val

class Solution:
    def deleteNode(self,head,val):
        if head.val==val:
            return head.next 
        pre=ListNode(head)
        cur=head
        while cur:
            if cur.val==val:
                pre.next=cur.next 
                return head
            pre=cur
            cur=cur.next 
            