# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 只需要中序遍历找到，第一个升序顺序错乱最大值节点，和最后一个升序顺序错乱的最小值节点。然后交换两个节点val即可。
        self.res=[]
        def DFS(node):
            if not node:
                return
            DFS(node.left)
            self.res.append(node)
            DFS(node.right)
        
        DFS(root)
        x=None
        y=None
        pre=self.res[0]
        
        for i in range(1,len(self.res)):
            if pre.val>self.res[i].val:
                y=self.res[i] # y在遍历过程中不断更新，是顺序错乱的最小值结点
                if not x:
                    x=pre # x 是第一个升序遍历顺序错乱最大值结点
            pre=self.res[i]
        
        if x and y:
            x.val,y.val=y.val,x.val
        
        
            
                
            
        
        