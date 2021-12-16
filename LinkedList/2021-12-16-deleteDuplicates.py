# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy=ListNode(101,head)
        # 用pre来控制前驱结点
        pre=dummy
        cur=head
        while cur and cur.next:
            post=cur.next # 用post来控制后驱结点
            while cur.val!=post.val: # 当值不等时，cur向链表后端移动
                pre=cur
                cur=cur.next
                post=cur.next
            if not cur.next: # 当cur移动到链表最后一位，即cur.next=None,返回结果
                return dummy.next
            if cur.val==post.val: # 若两值相等
                deleteVal=cur.val # 记录下待删除的结点的val
                if not post.next: # post已是最后一个结点，则将pre结点直接设为尾结点，返回
                    pre.next=None
                    return dummy.next
                while post and post.val==deleteVal: # post不是最后一个结点且值都等于待删除的结点，一直向后遍历
                    post=post.next 
                #最终pre和post中间所夹的结点即为所有重复结点
                pre.next=post # pre的下一个结点设为post，即过滤了中间所有结点
                cur=post  
        return dummy.next

# 官方题解更简单写法：重复的元素在链表中出现的位置是连续的
# 从指针cur指向链表的dummy node，随后开始对链表进行遍历。
# 如果当前cur.next与cur.next.next对应的元素相同，那么我们就需要将cur.next以及所有后面拥有相同元素值的链表节点全部删除。
# 我们记下这个元素值x，随后不断将cur.next从链表中移除，直到cur.next为空节点或者其元素值不等于x为止。此时，我们将链表中所有元素值为x的节点全部删除。
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy=ListNode(101,head)
        cur=dummy
        while cur.next and cur.next.next:
            if cur.next.val==cur.next.next.val:
                x=cur.next.val
                while cur.next and cur.next.val==x:
                    cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next
'''            