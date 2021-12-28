# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归解法
class Solution:
    def postorderTraversal(self, root):
        def postOrder(root,res):
            if root.left:
                postOrder(root.left,res)
            if root.right:
                postOrder(root.right,res)
            res.append(root.val)
        if not root:
            return []
        res=[]
        postOrder(root,res)
        return res
    
# 迭代解法：
class Solution:
    def postorderTraversal(self, root):
        output=[]
        stack=[]
        if not root:
            return []
        stack.append(root)
        while stack:
            cur=stack[-1]
            output.append(cur.val)
            stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return output[::-1]
        