# 题目：剑指 Offer 24. 反转链表，https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre=None
        cur=head
        while cur:
            post=cur.next
            cur.next=pre
            pre=cur
            cur=post # cur.next已经改变,指向了pre,所以这里再往后遍历时,用前面记录的post
        return pre