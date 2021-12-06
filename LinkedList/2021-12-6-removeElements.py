# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy=ListNode(0) # 构建虚拟结点来识别前驱结点
        dummy.next=head # 从内存中开辟一块新空间存指针，使得其值与head相同
        # 指针：字符串、整型、浮点型变量值，都是通过开辟新空间来赋值存储，其余则是通过指针指向同一块内存来存储
        pre=dummy # pre和dummy都是node，他们指向同一块内存，因此，pre的指向改变即dummy的指向改变
        while pre:
            if pre.next.val==val:
                pre.next=pre.next.next
            else:
                pre=pre.next          
        return dummy.next # dummy和pre同内存，因此pre改动，dummy也会发生改动，但是head是保持不变的
