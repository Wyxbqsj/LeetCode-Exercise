class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
'''
方法一由于是自顶向下递归，因此对于同一个节点，函数depth会被重复调用，导致时间复杂度较高。
如果使用自底向上的做法，则对于每个节点，函数depth只会被调用一次。

自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。
如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。
'''

# 递归肯定是要先从顶层把值传下去，关键要看有没有把底层的返回上去
# 自底向上递归
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(r):
            if not r:
                return 0
            leftheight=depth(r.left)
            rightheight=depth(r.right)
            # -1表示子树不平衡
            if leftheight==-1 or rightheight==-1 or abs(leftheight-rightheight)>1:
                return -1
            else:
                return max(leftheight,rightheight)+1
        
        return depth(root)>0
        
        