# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 由于无法定位到上一个结点，所以将node与node.next的结点的值进行交换，再删除结点即可
        temp=node.val
        node.val=node.next.val
        node.next.val=temp
        node.next=node.next.next
        
        #由于node一定会被删除，所以其实也不是必须要交换，将原来node.next的结点的值保存下来即可
        '''
        node.val=node.next.val
        node.next=node.next.next
        '''
        