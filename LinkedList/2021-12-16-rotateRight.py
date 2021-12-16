# Definition for singly-linked list.
'''
题意:将链表每个节点向右移动k 个位置，相当于把链表的后面 k % len个节点移到链表的最前面。（len为链表长度）
所以本题的步骤:
1.求链表长度；
2.找出倒数第 k+1 个节点；
3.链表重整: 将链表的倒数第 k+1个节点和倒数第k个节点断开，并把后半部分拼接到链表的头部。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        if k==0 or not head or not head.next:
            return head
        _len=0
        cur=head
        # 1.求链表长度
        while cur:
            _len+=1
            cur=cur.next 
        k=k%_len
        if k==0:
            return head
        # 找出倒数第k+1个结点
        slow,fast=head,head
        while k:
            fast=fast.next
            k-=1
        '''
        fast比slow快k步，初始时，slow指向第一个结点，fast指向第k+1个结点
        当到达循环终点fast.next=None,即fast指向最后一个结点
        假设fast和slow同步走了m步，即(k+1)+m=_len
        因此m=_len-(k+1)
        所以此时slow从第1个结点走到了第_len-(k+1)个结点，即slow 指向倒数第（k+1）个结点
        '''
        # slow 指向倒数第（k+1）个结点
        while fast.next:
            slow=slow.next 
            fast=fast.next 
        newHead=slow.next # newHead指向倒数第k个结点
        fast.next=head
        slow.next=None
        return newHead
        
        
            
        