# 二叉树的遍历：数据结构规定，在遍历过程中，先遍历左子树，再遍历右子树；故得出（深度遍历上的）三种遍历方式
'''
!!!对于二叉树，有深度遍历和广度遍历，深度遍历：前序、中序、后序三种；广度遍历即我们平常所说的层次遍历。
四种主要的遍历思想为：主要看根节点是第几个访问
(1)前序遍历：根结点 ---> 左子树 ---> 右子树
(2)中序遍历：左子树---> 根结点 ---> 右子树
(3)后序遍历：左子树 ---> 右子树 ---> 根结点
(4)层次遍历：只需按层次遍历即可
'''

class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right
# 递归解法
# (1)前序遍历：
def preOrder(root: TreeNode):
    if not root:
        return None
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)
# (2)中序遍历：
def inOrder(root:TreeNode):
    if not root:
        return None
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)
# (3)后序遍历：
def postOrder(root:TreeNode):
    if not root:
        return None
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)
    

            









