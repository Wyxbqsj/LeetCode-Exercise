# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inOrder(root,res):
            if not root:
                return
            inOrder(root.left,res)
            res.append(root.val)
            inOrder(root.right,res)
        
        if not root:
            return 
        res=[]
        inOrder(root,res)
        minGap=10000000
        for i in range(1,len(res)):
            curGap=res[i]-res[i-1]
            if curGap<=minGap:
                minGap=curGap
        return minGap
            
            
        