# 题目：剑指 Offer 27. 二叉树的镜像，https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

''' 
解法一： 递归解法
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return # 遍历到终点，返回空
        tmp=root.left
        root.left=self.mirrorTree(root.right) # 在这里root.left会发生改变，所以在这一步之前要将原来的值保存下来，为下一步使用
        root.right=self.mirrorTree(tmp)
        return root
'''

'''
解法二：迭代，利用辅助栈
利用栈遍历树的所有节点cur，并交换每个cur的左 / 右子节点。
'''
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        stack=[root]
        while stack:
            cur=stack.pop()
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            cur.left,cur.right=cur.right,cur.left
        return root
            