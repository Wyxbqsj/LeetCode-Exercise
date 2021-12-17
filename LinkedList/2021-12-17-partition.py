# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small=ListNode(0)
        curs=small
        large=ListNode(0)
        curl=large
        cur=head
        while cur:
            if cur.val<x:
                curs.next=cur
                curs=curs.next
            else:
                curl.next=cur
                curl=curl.next
            cur=cur.next     
        curs.next=large.next # 注意是怎么把large和small这两个链表接起来的
        curl.next=None # 一定要将新建的链表尾结点的next设为None，这个和后台的判定程序有关，十分重要
        return small.next
           
           
           
            
            