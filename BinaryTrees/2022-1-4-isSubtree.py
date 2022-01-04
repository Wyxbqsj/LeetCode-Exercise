# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSametree(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                if p.val==q.val:
                    return isSametree(p.left,q.left) and isSametree(p.right,q.right)
                else:
                    return False
        if not root:
            return False
        # 一个树是另一个树的子树 则
        # 要么这两个树相等
        # 要么这个树是左树的子树
        # 要么这个树是右树的子树
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) or isSametree(root,subRoot)
            
            
            
            
