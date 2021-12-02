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
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2 #哪里return，返回到哪里去，而不是整段代码遇到return就直接结束了
        if list2 is None:
            return list1
        elif list1.val<list2.val:
            list1.next=self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next=self.mergeTwoLists(list1,list2.next)
            return list2


x=Solution()
list1=ListNode(0)
list1=createList(list1,[1,2,4],0)
list2=ListNode(0)
list2=createList(list2,[1,3,4],0)
a=x.mergeTwoLists(list1,list2)
while a:
    print(a.val)
    a=a.next
