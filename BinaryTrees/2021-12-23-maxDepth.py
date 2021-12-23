# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 层次遍历的暴力解法
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        queue=[root]
        count=0
        next_queue=[]
        while queue:
            cur=queue[0]
            queue.pop(0)
            if cur:
                if cur.left:
                    next_queue.append(cur.left)
                if cur.right:
                    next_queue.append(cur.right)
            if len(queue)==0:
                queue=next_queue
                next_queue=[]
                count+=1
        return count
            
        
                    