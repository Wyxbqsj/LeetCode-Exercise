# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        curLevel=[root]
        nextLevel=[]
        res=[]
        count=0
        while curLevel:
            count+=1
            tmp=[]
            for cur in curLevel:
                tmp.append(cur.val)
                if cur.left:
                    nextLevel.append(cur.left)
                if cur.right:
                    nextLevel.append(cur.right)
            if count%2==0:
                tmp=tmp[::-1]
            res.append(tmp)
            if len(nextLevel)==0:
                return res
            else:
                curLevel=nextLevel
                nextLevel=[]
    
                    
            