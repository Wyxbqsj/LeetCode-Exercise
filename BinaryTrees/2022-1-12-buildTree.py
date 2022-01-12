# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
preorder第一个元素为root，在inorder里面找到root，在它之前的为左子树（长l1），之后为右子树（长l2）。
preorder[1]到preorder[l1]为左子树,之后为右子树，分别递归。
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
       
        val=preorder.pop(0)
        root=TreeNode(val)
        i=inorder.index(val)
  
        root.left=self.buildTree(preorder[:i],inorder[:i])
        root.right=self.buildTree(preorder[i:],inorder[i+1:])
   
        return root
        


