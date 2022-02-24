# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow,fast=head,head.next
        while slow!=fast: # 若slow==fast，快慢指针相遇，不进入循环，则返回True
            if not fast or not fast.next: # 若遍历到链表末尾，则说明五环，返回False. 因为有环的话，fast永远不会走到终点，一直走，直到与slow相遇
                return False
            slow=slow.next
            fast=fast.next.next 
        return True


