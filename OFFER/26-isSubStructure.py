# Definition for a binary tree node.
# 题目：剑指 Offer 31. 栈的压入、弹出序列，https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

''' 注意！！！这道题判断子结构和判断子树是不同的！！！
子结构只需要A树中有一段与B相同
子树需要A树中某个结点及其后代所有的结点与B相同，所以包含的递归是判断两个树是否完全相等
但判断子结构不需要完全相等的，只要有一段与B相同即可！不需要整棵子树都一样！！！
'''
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def compareTree(p,q):
            if not p and not q:
                return True
            elif not p: # 母树空了，但子树不空，则B肯定不是A的子结构
                return False
            elif not q: # B遍历完了，都满足，则返回True
                return True
            if p.val==q.val:
                return compareTree(p.left,q.left) and compareTree(p.right,q.right)
            else:
                return False
        
        # 判断B是不是A的子树，所以分三步即可：A、B是否是相同的树；B是A左树的子树；B是A右树的子树
        # 题目已经讲了，空树不是任意一个树的子结构，因此递归出口，即判断A或B是否为空
        if not B or not B:
            return False
        return compareTree(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)