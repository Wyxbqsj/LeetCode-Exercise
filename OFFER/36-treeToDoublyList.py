# 题目：剑指 Offer 36. 二叉搜索树与双向链表，https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1.排序链表：中序遍历BST即可得到一个排好序的数组，中序遍历：left->cur->right
    # 2.双向链表：在构建相邻结点之间的关系时，设前驱结点为pre，当前结点为cur，不仅要构建pre.right=cur，还要构建cur.left=pre
    # 3.循环链表：设链表头结点为head，尾结点为tail，则应构建head.left=tail; tail.right=head
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            if self.pre:
                self.pre.right=cur
                cur.left=self.pre
            else:
                self.head=cur
            self.pre=cur # self.pre保存的是cur，因为cur在不断往后走，pre也需要往后走
            dfs(cur.right)
        
        if not root: return
        self.pre=None
        self.head=None
        dfs(root)
        self.head.left=self.pre
        self.pre.right=self.head
        return self.head