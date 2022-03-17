# 题目：剑指 Offer 07. 重建二叉树，https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

# 前序遍历：[root,left,right]
# 中序遍历：[left,root,right]
class Solution:
    def buildTree(self,preOrder,inOrder):
        if not preOrder or not inOrder: # 递归函数一定要有递归出口
            return None
        cur=preOrder.pop(0) # 注意pop()函数默认参数是-1，弹出list顶的元素，所以一定要写成pop(0)
        i=inOrder.index(cur) # 获取根节点在inOrder中的索引
        root=TreeNode(cur)
        # 注意每次preOrder都弹出一个起点元素，因此preOrder的长度都会变小，注意边界的选择
        root.left=self.buildTree(preOrder[:i],inOrder[:i]) 
        root.right=self.buildTree(preOrder[i:],inOrder[i+1:]) # 由于preOrder中弹出来了一位，因此左子树在preOrder中可以直接从i取，不用往后跳一位
        return root
        