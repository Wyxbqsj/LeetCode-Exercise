# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur=head
        count=0
        while cur:
            cur=cur.next
            count=count+1
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        if count%2==0:
            return slow.next
        else:
            return slow

# 由数组nums构建链表
def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head
    
'''
如何不用判断链表的奇偶数，直接返回就满足题目的要求：
当循环条件是 while fast.next and fast.next.next时，返回的是第一个中间节点（当有两个中间节点）
当循环条件是 while fast and fast.next时，返回的是第二个中间结点（当有两个中间结点）
因此本道题的代码可以写成：
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
'''
