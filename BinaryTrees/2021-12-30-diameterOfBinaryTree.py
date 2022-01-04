# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(root):
            if not root:
                return 0, 0

            left_dep, left_dia =depth(root.left) # 左子树的最大深度和左子树的直径
            right_dep, right_dia =depth(root.right) # 右子树的最大深度和右子树的直径
            max_dep = max(left_dep, right_dep) + 1 # 树的最大深度（节点的个数）等于左子树和右子树深度最大的那个再加上1（根节点）
            max_dia = max(left_dia, right_dia, left_dep+right_dep) # 树的最大直径等于：左子树的最大直径、右子树的最大直径、自己本身所在的树的直径（直径看的是边，不需要再加1），三者中的最大值
            return max_dep, max_dia # 返回值有两个：子树的最大深度和子树的直径
        
        x,y = depth(root)
        return y
        
 
                
                