# 题目：剑指 Offer 22. 链表中倒数第k个节点，https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return 
        fast,slow=head,head
        while k:
            fast=fast.next
            k-=1
        while fast:
            fast,slow=fast.next,slow.next
        return slow