# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 暴力解：
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         def tranf(l):
#             pre=None
#             cur=l
#             while cur:
#                 post=cur.next 
#                 cur.next=pre
#                 pre=cur
#                 cur=cur.next 
#             return pre
        
#         def compute(l):
#             ans=0
#             cur=l
#             while cur:
#                 ans=ans*10+cur.val
#                 cur=cur.next 
#             return ans             
        
#         l1new=tranf(l1)
#         ans1=compute(l1new)
#         l2new=tranf(l2)
#         ans2=compute(l2new)
#         res=ans1+ans2
#         head=ListNode(res%10)
#         cue=head
#         while res>1:
#             res=res/10
#             cue.next=ListNode(res%10)
#             cue=cue.next 
#         head=tranf(head)
#         return head

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 题目已经说明是逆序表示，补全一个短链表并不需要在链表头添加0结点，在链表为空时，直接加0结点即可
        res=cur=ListNode(0)
        carry=0
        while l1 or l2:
            if not l1:
                l1=ListNode(0)
            if not l2:
                l2=ListNode(0)
            sum=l1.val+l2.val+carry
            if sum>=10:
                carry=1
                cur.next=ListNode(sum%10)
            else:
                carry=0
                cur.next=ListNode(sum)
            l1=l1.next
            l2=l2.next
            cur=cur.next
        if carry==1:
            cur.next=ListNode(carry)
        return res.next    
            
            
        
                
        
                