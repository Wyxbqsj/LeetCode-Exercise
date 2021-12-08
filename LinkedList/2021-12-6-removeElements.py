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
        # 在C++中：字符串、整型、浮点型三种类型，都是通过开辟新空间来赋值存储，即他们不共享内存，
        # 其余类型的变量（如自定义的类）则是通过指针指向同一块内存来存储，即他们共享内存
        # 而在Python中，所有的变量都是通过指针来存储，即所有变量都共享内存，只是这三种类型共享的是不可变的内存，而其他类型的内存空间是可变的
        pre=dummy # pre和dummy共享内存
        while pre:
            if pre.next.val==val:
                pre.next=pre.next.next
            else:
                pre=pre.next # pre和pre.next共享内存         
        return dummy.next # dummy和最初的pre共享内存，即dummy.next保存了头结点以pre为变量的列表的头结点，因此返回dummy.next，但是head是始终保持不变的，不可返回head
