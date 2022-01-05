# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 遍历到终点，返回
        if not root1 and not root2:
            return
        # 若当前位置树1结点为空，树2不为空，则把树2直接链接到最终结果树root上
        elif not root1:
            return root2
        # 若当前位置树2结点为空，树1不为空，则把树1直接链接到最终结果树root上
        elif not root2:
            return root1
        # 都不空有值时，最终结果树root的当前结点的值val是两节点值之和
        val=root1.val+root2.val
        root=TreeNode(val)
        # 左子树是树1左子树和树2左子树合并的结果树
        root.left=self.mergeTrees(root1.left,root2.left)
        # 右子树是树1右子树和树2右子树合并的结果树
        root.right=self.mergeTrees(root1.right,root2.right)
        return root
            