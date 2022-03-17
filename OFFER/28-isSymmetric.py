# 题目：剑指 Offer 28. 对称的二叉树，https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
解法一：迭代，BFS+回文串
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        curLevel=[root]
        nextLevel=[]
        while curLevel:
            tmp=[] # 要用一个list存储每一层的结点值判断回文串，而不是用存的结点判断回文串
            for cur in curLevel:
                if cur:
                    tmp.append(cur.val)
                    nextLevel.append(cur.left)
                    nextLevel.append(cur.right)
                else:
                    tmp.append(-1)
            if tmp!=tmp[::-1]:
                return False
            curLevel=nextLevel
            nextLevel=[]
        return True
'''

# 方法二：递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(L,R):
            if not R and not L:
                return True
            elif not R or not L:
                return False
            if L.val==R.val:
                return symmetric(L.left,R.right) and symmetric(L.right,R.left)
            else:
                return False   
        if not root:
            return True
        return symmetric(root.left,root.right) 