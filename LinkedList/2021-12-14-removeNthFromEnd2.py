# Definition for singly-linked list.
from typing import List

# 快慢指针方法
'''
1）为了方便，我们在原有链表前面设置一个dummy node，dummy node的好处在于: 
当我们是要删除一个结点时，我们可以定位到被删除结点的前置结点，
然后将前置结点的后续指针指向被删除结点的后续结点，则可完成删除。
而头结点无前置结点，因此我们用dummy node指向它来控制它的前驱结点

2）我们设置两个指针，两个指针初始状态都指向dummy node，
!!!指针fast先走n步，然后指针fast和指针slow同步往前继续遍历链表，
直到fast的后续结点为空，此时指针slow到达被删除结点的前置结点
其实在快慢指针方法中，fast用来控制边界条件，slow用来定位结点
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0,head)
        slow,fast=dummy,dummy
        '''
        由于我们需要找到倒数第n个节点，fast和slow同时对链表进行遍历，并且初始时fast比slow超前n个节点。
        当fast遍历到链表的末尾(即fast=None)时slow就恰好处于倒数第n个节点。
        所以当fast.next=None时，slow恰好位于倒数第n个节点的前驱节点
        '''
        for i in range(n): # 让fast先比slow多走n步
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next
            
            