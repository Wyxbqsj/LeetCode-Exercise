class ListNode:
    def __init__(self,x) -> None:
        self.val=x
        self.next=None
# 题解：https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
# 从同一起点出发，fast每次走两步，slow每次走一步，因此fast=2slow (1)
# 当他们俩相遇时，即fast比slow多走了n圈，假设环上结点数量是b，则fast=slow+nb (2)
# 综合(1)(2)得到：slow=nb，fast=2nb
# 从链表头结点走到入环点的距离假设是a，所以走a+nb步都能走到入环点（每走一圈都会回到入环点）
# 由于slow已经走了nb步，因此slow再走a步就是入环点了
# 所以从head开始，和slow一起走，相遇时刚好就走了a步

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow,fast=head,head # 需从同一起点出发，才有这个性质slow=nb，fast=2nb
        
        while True:
            if not fast or not fast.next:
                return
            slow,fast=slow.next,fast.next.next 
            if slow==fast:
                break
            
        fast=head
        while slow!=fast:
            slow,fast=slow.next,fast.next # 同时走，都走一步
        return slow