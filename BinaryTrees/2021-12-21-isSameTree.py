# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 之前的想法：通过遍历获得两棵树遍历得到的list，最后判断两个list是否相同
# 无法AC的原因：两种遍历序列才可以确定一棵树。相同的序列且仅靠一个遍历序列，树的形状有很多
'''
给定 先序+中序 or 后序+中序 可以唯一确定一颗二叉树
而 先序+后序 不能
	  A
	 /
	B
前序遍历： AB, 后序遍历： BA
	A
	 \
	  B
前序遍历： AB, 后序遍历： BA
'''

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            if p.val!=q.val:
                return False
            else:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)