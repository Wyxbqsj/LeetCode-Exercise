# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root) -> int:
        self.sum=0
        def treeSum(node): # treeSum有两个作用：1.返回每个节点及其左右左右之和；2.计算每个结点的坡度并对其求和sum
            if not node:
                return 0
            left=treeSum(node.left)
            right=treeSum(node.right)
            self.sum+=abs(left-right)
            return node.val+left+right
            
        if not root:
            return 0
        treeSum(root)
        return self.sum
        
            
            
            
        
        
        
            