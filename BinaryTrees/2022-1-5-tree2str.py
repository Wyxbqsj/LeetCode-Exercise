# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root) -> str:
        # 遍历到终点（叶子结点的下一个结点），返回空
        if not root:
            return ''
        # 当前结点是叶子结点，返回当前结点的值
        if not root.left and not root.right:
            return str(root.val)
        # 当前节点无左孩子有右孩子，返回root()(right)
        if not root.left and root.right:
            return '()'+'('+self.tree2str(root.right)+')'
        # 当前结点无右孩子有左孩子，返回root(left)
        if root.left and not root.right:
            return '('+self.tree2str(root.left)+')'
        # 当前结点既有左孩子又有右孩子，返回root(left)(right)
        return '('+self.tree2str(root.left)+')'+'('+self.tree2str(root.right)+')'