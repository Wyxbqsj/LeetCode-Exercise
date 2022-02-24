# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return -1
        visited=set()
        cur=head
        while cur.next:
            if cur not in visited:
                visited.add(cur)
            else:
                return cur
        return -1
        