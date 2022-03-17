# 题目：剑指 Offer 34. 二叉树中和为某一值的路径，https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# ！！！回溯算法
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res,path=[],[]
        def backTracking(root,tar):
            if not root:
                return
            path.append(root.val)
            tar-=root.val
            if tar==0 and not root.left and not root.right:
                # 值得注意的是，list时可变对象，记录路径时若直接执行 res.append(path) ，则是将 path 对象加入了 res ；
                # 后续 path 改变时， res 中的 path 对象也会随之改变。
                # ！！！python传参传对象，可变对象可变，不可变对象不可变
                res.append(path[:]) # 将path复制一份添加进来，而非用原来的path
            backTracking(root.left,tar)
            backTracking(root.right,tar)
            path.pop() # 已经到叶子结点，但不满足tar，则回溯到上一结点，朝另一条岔路走
        backTracking(root,target)
        return res
            
            
            