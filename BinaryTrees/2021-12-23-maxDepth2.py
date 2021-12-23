# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 深度优先搜索：
# 如果我们知道了左子树和右子树的最大深度为l和r，那么该二叉树的最大深度为max(l,r)+1
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            leftheight=self.maxDepth(root.left)
            rightheight=self.maxDepth(root.right)
            return max(leftheight,rightheight)+1