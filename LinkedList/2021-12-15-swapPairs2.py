# Definition for singly-linked list.
# 递归解法
'''
如果链表中至少有两个节点，则在两两交换链表中的节点之后，原始链表的头节点变成新的链表的第二个节点，原始链表的第二个节点变成新的链表的头节点。
链表中的其余节点的两两交换可以递归地实现。
在对链表中的其余节点递归地两两交换之后，更新节点之间的指针关系，即可完成整个链表的两两交换。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead=head.next # 新链表的头结点
        head.next=self.swapPairs(newHead.next) # 原始链表中剩余链表的头结点变为newHead.next
        newHead.next=head # 交换后原剩余链表的新的头结点变为新链表的头结点的next
        return newHead
        
        
        