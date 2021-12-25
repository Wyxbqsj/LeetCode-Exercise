# Definition for a binary tree node.
# 注意这道题平衡树的定义概念：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
# 是每个结点的左右子树都要满足，而非只需要根节点满足

# 自顶向下的递归
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(r):
            if not r:
                return 0
            else:
                hleft=depth(r.left)
                hright=depth(r.right)
                return max(hleft,hright)+1
        
        if not root:
            return True
        else:
            return abs(depth(root.left)-depth(root.right)<=1) and self.isBalanced(root.left) and self.isBalanced(root.right)