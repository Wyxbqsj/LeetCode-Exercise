# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def createList(listClass,list,i):
    if i<len(list):
        if list[i]==None:
            return None
        else:
            listClass=ListNode(list[i])
            listClass.next=createList(listClass.next,list,i+1)
            return listClass
    return listClass

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur=head
        while cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head

x=Solution()
head=ListNode(0)
head=createList(head,[1,1,2],0)
a=x.deleteDuplicates(head)
while a:
    print(a.val)
    a=a.next

                              
            
            
