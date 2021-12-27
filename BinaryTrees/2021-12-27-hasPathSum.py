# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root:TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        # 当题目中提到了叶子节点时，正确的做法一定要同时判断节点的左右子树同时为空才是叶子节点。
        if not root.left and not root.right:
            return root.val==targetSum
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)
        
            
            