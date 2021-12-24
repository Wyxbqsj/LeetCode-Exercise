# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
二叉搜索树（Binary Search Tree），简写BST，是满足某些条件的特殊的二叉树：
任何一个节点的左子树上的点，都必须小于当前节点。任何一个节点的右子树上的点，都必须大于当前节点。
任何一棵子树，也都满足上面两个条件。另外二叉查找树中，是不存在重复节点的。
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l=len(nums)
        # 递归终止条件
        if l==0:
            return None
        
        if l>0: 
            mid=l//2
            root=TreeNode(nums[mid])
            if mid-1>=0:
                root.left=self.sortedArrayToBST(nums[:mid])
            if mid+1<l:
                root.right=self.sortedArrayToBST(nums[mid+1:])
        return root
        