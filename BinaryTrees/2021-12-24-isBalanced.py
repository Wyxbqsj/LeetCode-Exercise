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
        # 计算高度的depth都是自底向上计算的，这里所说的自顶向下，主要是isBalanced()函数的else部分
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
            # 三个判别式，从左到右执行，先判断头结点是否平衡，再分别判断两个子树，这是典型的自顶向下
            return abs(depth(root.left)-depth(root.right)<=1) and self.isBalanced(root.left) and self.isBalanced(root.right)
