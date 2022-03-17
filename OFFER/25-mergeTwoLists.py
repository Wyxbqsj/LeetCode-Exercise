# 题目：剑指 Offer 25. 合并两个排序的链表，https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1, cur2 = l1, l2
        head=ListNode(0)
        cur=head
        while cur1 and cur2:
            if cur1.val>=cur2.val:
                cur.next=ListNode(cur2.val)
                cur2=cur2.next 
            else:
                cur.next=ListNode(cur1.val)
                cur1=cur1.next
            cur=cur.next
        if cur1:
            cur.next=cur1
        if cur2:
            cur.next=cur2
            
        
        