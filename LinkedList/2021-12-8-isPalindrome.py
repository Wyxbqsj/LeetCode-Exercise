# Definition for singly-linked list.
# ！！！链表题中看到O(n)时间复杂度且O(1)空间复杂度可以考虑快慢指针，就相当于数组题看到O(n)时间复杂度且O(1)空间复杂度可以考虑双指针一样。
# 回文链表一定是对称的，因此找到链表的中点后，比较前后两段结点的值即可
'''解题思路：
1. 用快慢指针找到链表的中点
2. 将后半段链表逆序
3. 遍历后半段链表（奇数时后半段链表的结点数目一定小于前半段），对比与前半段链表的结点值
4. 遇到不等返回False, 遍历到终点则返回True
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 反转链表
        def reverse(h):
            pre=None
            cur=h
            while cur:
                post=cur.next
                cur.next=pre
                pre=cur
                cur=post
            return pre
        if not head:
            return True      
        
        # 快慢指针找到链表的中点：slow        
        slow,fast=head, head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next 
        before=head # 前半段链表
        after=slow.next #后半段链表
        after=reverse(after)
        while after:
            if after.val!=before.val:
                return False
            after=after.next 
            before=before.next
        return True
    
    
          

