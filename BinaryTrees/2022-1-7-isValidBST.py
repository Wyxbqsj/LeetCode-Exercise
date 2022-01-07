# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 注意该题是左子树上所有节点的值均小于它的根节点的值，而非一个左节点的值小于根节点即可
''' 
二叉搜索树的性质：
（1）如果该二叉树的左子树不为空，则左子树上所有节点的值均小于它的根节点的值； 
（2）若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
（3）它的左右子树也为二叉搜索树。
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 设计一个递归函数 helper(root,lower,upper)，考虑以root为根节点的子树，判断子树中所有结点的值都在lower-upper的范围内
        # 函数递归调用的入口为 helper(root, -inf, +inf)， inf 表示一个无穷大的值。
        def helper(node, lower=float('-inf'),upper=float('inf'))->bool:
            if not node:
                return True
            val=node.val
            if val<=lower or val>=upper: # 若当前结点值不在规定范围内，返回false
                return False
            
            if not helper(node.right,val,upper): # 如果右子树不满足
                return False
            if not helper(node.left,lower,val): # 如果左子树不满足
                return False
            return True
        return helper(root)
            