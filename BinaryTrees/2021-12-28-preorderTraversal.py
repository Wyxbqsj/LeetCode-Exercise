# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        def preOrder(root,res):
            res.append(root.val)
            if root.left:
                preOrder(root.left,res)
            if root.right:
                preOrder(root.right,res)
        if not root:
            return []
        res=[]
        preOrder(root,res)  
        return res

 
# 注意！！！只有之后把叶子节点的结果return，一层一层的return上去，根节点最后才能return出来东西
class Solution:
    def preorderTraversal(self, root):
        def preOrder(root,res):
            if not root:
                return res
            res.append(root.val)
            if root.left:
                preOrder(root.left,res)
            if root.right:
                preOrder(root.right,res)
            return res # 如果不写这句话，整个代码只return结点为空时的res，不为空的树最后啥东西都不返回
        res=[]
        return preOrder(root,res)
