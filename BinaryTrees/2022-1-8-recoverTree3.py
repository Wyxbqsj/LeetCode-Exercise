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
        莫里斯遍历：该算法能将非递归的中序遍历空间复杂度降为 O(1)。

Morris 遍历算法整体步骤如下（假设当前遍历到的节点为 x）：
1. 如果 x 无左孩子，则访问 x 的右孩子，即 x = x.right。
2. 如果 x 有左孩子，则找到 x 左子树上最右的节点（即左子树中序遍历的最后一个节点，x 在中序遍历中的前驱节点），我们记为 predecessor。根据 predecessor 的右孩子是否为空，进行如下操作。
(1) 如果 predecessor 的右孩子为空，则将其右孩子指向 x，然后访问 x 的左孩子，即 x = x.left。
(2) 如果 predecessor 的右孩子不为空，则此时其右孩子指向 x，说明我们已经遍历完 x 的左子树，我们将 predecessor 的右孩子置空，然后访问 x 的右孩子，即 x = x.right。
3. 重复上述操作，直至访问完整棵树。

其实整个过程我们就多做一步：将当前节点左子树中最右边的节点指向它，这样在左子树遍历完成后我们通过这个指向走回了 x，且能再通过这个知晓我们已经遍历完成了左子树，而不用再通过栈来维护，省去了栈的空间复杂度。      
        """
        x=None # x,y记录发生错误的两个结点
        y=None
        pre=None # 记录中序遍历当前结点的前驱
        tmp=None # 用来完成Morris遍历的寻找前驱的指针
        while root:
            if root.left:
                tmp=root.left
                while tmp.right and tmp.right!=root:
                    tmp=tmp.right
                if tmp.right is None:
                    tmp.right=root
                    root=root.left
                else:
                    if pre and pre.val>root.val:
                        y=root
                        if not x:
                            x=pre
                    pre=root
                    tmp.right=None
                    root=root.right
            else:
                if pre and pre.val>root.val:
                    y=root
                    if not x:
                        x=pre
                pre=root
                root=root.right
        
        if x and y:
            x.val,y.val=y.val,x.val
        