# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur=head
        count=0
        while cur:
            cur=cur.next
            count+=1
        ans=0
        while head:
            count=count-1
            ans=ans+2**(count)*head.val
            head=head.next
        return ans

# 可以不用知道链表的长度，也能确定2的指数
'''
每读取链表的一个节点值，可以认为读到的节点值是当前二进制数的最低位；
当读到下一个节点值的时候，需要将已经读到的结果乘以 22，再将新读到的节点值当作当前二进制数的最低位；
如此进行下去，直到读到了链表的末尾。
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur=head
        ans=0
        while cur:
            ans=ans*2+cur.val # 当前cur是最低位，将上一轮得到的值乘以2
            cur=cur.next
        return ans
'''
            
            