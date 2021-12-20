# 注意不再是用print记录访问，而是返回一个list
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''递归解法
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        # 函数inorderTraversal()和函数inOrder()是两个函数，不加self的res都是局部变量，均不相同
        # 加了self后，就是属于Solution类的同一个变量，一个变，另一个也变
        self.res=[]
        self.inOrder(root)
        return self.res
    
    def inOrder(self, node:TreeNode):
        if node.left:
            self.inOrder(node.left)
        self.res.append(node.val)
        if node.right:
            self.inOrder(node.right)
'''           
 # 非递归解
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        res=[]
        stack=[]
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack[-1]
                res=root.val
                stack.pop()
                root=root.right
        return res
            
