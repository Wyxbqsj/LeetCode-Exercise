# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':              
        if (root.val>p.val and root.val<q.val) or (root.val>q.val and root.val<p.val): # 更简洁的写法这个判断句可以删掉，但有他在效果更好
            return root
        elif root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)       
        return root

# 本题思路利用二叉搜索树的特点
# 如果p、q的值都小于root，说明p q 肯定在root的左子树中；
# 如果p q都大于root，说明肯定在root的右子树中，
# 如果一个在左一个在右 则说明此时的root记为对应的最近公共祖先

                
                    
                