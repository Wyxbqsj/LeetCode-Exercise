
# 看到二叉搜索树就想这句话，不会的请背诵：中序遍历二叉搜索树等于遍历有序数组
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        # 中序遍历BST得到是有序数组      
        def dfs(root,res):
            if not root:
                return
            dfs(root.left,res)
            res.append(root.val)
            dfs(root.right,res)
        
        if not root:
            return []
        dics={}
        
        res=[]
        dfs(root,res)
        for i in res:
            if i not in dics:
                dics[i]=1
            else:
                dics[i]+=1
        max_val=max(dics.values())
        ans=[]
        for item,val in dics.items():
            if val>=max_val:
                ans.append(item)
        return ans
        
            
            
            
            
        