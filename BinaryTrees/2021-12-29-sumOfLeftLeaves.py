# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def leftLeaves(root,sum):
            if root.left:
                if not root.left.left and not root.left.right: # 一定注意判断是不是叶子结点
                    sum.append(root.left)
                leftLeaves(root.left,sum)
            if root.right:
                leftLeaves(root.right,sum)
        
        ans=[]
        leftLeaves(root,ans)
        res=0
        for i in ans:
            res+=i.val
        return res