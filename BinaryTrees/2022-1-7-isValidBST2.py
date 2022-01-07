# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# BST中序遍历是有序数组，因此可以通过中序遍历判断是不是升序数组来判断BST
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:       
        self.res=[]       
        def BFS(node):
            if not node:
                return
            if node.left:
                BFS(node.left)
            self.res.append(node.val)
            if node.right:
                BFS(node.right)
        BFS(root)
        length=len(self.res)
        i=1
        while i<length:
            if self.res[i]<self.res[i-1]:
                return False
            i+=1
        return True
            
        
            