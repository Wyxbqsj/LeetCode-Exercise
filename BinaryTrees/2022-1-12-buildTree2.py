# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
postorder最后一个元素为root，在inorder里面找到root，在它之前的为左子树（长l1），之后为右子树（长l2）。
postorder[1]到preorder[l1]为左子树,之后为右子树，分别递归。
'''

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return 
        length=len(postorder)
        val=postorder.pop(length-1)
        root=TreeNode(val)
        i=inorder.index(val)
        root.left=self.buildTree(inorder[:i],postorder[:i])
        root.right=self.buildTree(inorder[i+1:],postorder[i:])
        return root
        