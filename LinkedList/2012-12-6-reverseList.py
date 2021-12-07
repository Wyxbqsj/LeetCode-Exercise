# Definition for singly-linked list.
'''
1.迭代需要三个指针，pre，cur，nxt，分别按顺序指向三个节点
2.三个指针的初始化：pre指向空节点，cur指向头结点head，nxt指向head.next
  因为head.next可能不存在，nxt在循环中定义，这样如果head为空就不会进入循环
3.迭代过程
  nxt指向cur.next
  cur.next指向pre
  pre移动到cur位置
  cur移动到nxt位置
4.当cur为空时，返回pre
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        这样写是不对的，pre是一个值为0的node，反转后的末尾应该是none,因此pre应初始化为none
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        '''
        pre=None
        cur=head
        while cur:
            post=cur.next
            cur.next=pre
            pre=cur
            cur=post
        return pre
            