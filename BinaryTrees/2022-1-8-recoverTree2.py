# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        用中序遍历的方式遍历这颗二叉搜索树，我们再增加一个辅助的pre指针，记录 上一个 节点的值。
        如果 当前节点的值，小于 上一个节点的值，这就找到了需要交换的节点。
        利用这种方式，就不需要额外的数组空间了。
        """
        self.x=None
        self.y=None
        self.pre=None
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not self.pre:
                self.pre=root
            else:
                if self.pre.val>root.val:
                    self.y=root
                    if not self.x:
                        self.x=self.pre
                self.pre=root
            dfs(root.right)
        
        dfs(root)
        
        if self.x and self.y:
            self.x.val,self.y.val=self.y.val,self.x.val