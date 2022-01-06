# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root) -> List[float]:
        if not root:
            return []
        cur_level=[root]
        next_level=[]
        res=[]
        while cur_level:
            length=len(cur_level)
            tmp=0
            for cur in cur_level:
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
                tmp+=cur.val
            avg=tmp/length
            res.append(avg)
            if len(next_level)==0:
                return res
            cur_level=next_level
            next_level=[]
            
                
            
            
            