# Definition for singly-linked list.
# 方法二：一次遍历，不另外写函数
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head.next or left==right:
            return head
        dummy=ListNode(0,head)
        count=1
        pre=dummy
        while pre.next and count<left:
            pre=pre.next
            count+=1
        cur=pre.next
        tail=cur
        while count<=right:
            nxt=cur.next
            
            # 开始翻转
            # 写这种指针指向交换问题：
            # 没有固定的顺序，但一定要能保证变量可以访问到每个节点，不要在换的过程中，有些节点就被丢掉了          
            '''
            pre.next=cur
            cur.next=tail
            按照这样写会有结点被丢掉，因为tail一直记录最初的cur的位置，保持不动，直接cur.next=tail，在while循环往后会有一些结点被漏掉
            '''
            # 等于号后面的都是会随着while的往前推进变化的
            cur.next=pre.next
            pre.next=cur
            tail.next=nxt
            cur=nxt
            count+=1
        return dummy.next
            