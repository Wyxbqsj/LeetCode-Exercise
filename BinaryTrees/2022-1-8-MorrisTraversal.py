from typing import List
# 中序遍历基本思路：左子树->根节点->右子树
# 莫里斯遍历思路：不使用任何辅助空间，强行把一棵二叉树改成一段链表结构。
'''
参阅文章：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/python3-die-dai-bian-li-chang-gui-jie-fa-dptw/
既然是链表，则每个结点cur，都要有前驱结点prev和后继结点post。
1.对于有右子树的结点cur，按照中序遍历的规则，他的后继结点post就是cur右子树上最左侧的结点
2.对于没有右子树的结点cur，按照中序遍历的规则，他的后继结点post就是其自下而上的父节点中第一个将其作为左子树的节点。
情况2有点难理解，我们可以换种理解方式：
3.对于有左子树的结点cur,按照中序遍历的规则,他的前驱结点prev就是cur左子树上最右侧的结点

因此结合1和3，就能得到莫里斯中序遍历的基本步骤：（中序遍历：左——中——右）
首先遍历左子树：（1）（2）
（1）当前结点没有左孩子，则访问当前结点cur，迭代遍历cur的右子树（cur=cur.right）
（2）当前结点有左孩子，满足情况3，故先找到cur的前驱结点prev，在将prev的后继节点设成cur，即完成了树到链表的转换：
     a) 找前驱节点：cur的前驱结点prev是cur左子树上最右侧的结点,故只要存在右孩子，一直prev = prev.right即可找到
     b) 将prev的后继节点设成cur: 如果前驱节点prev的右孩子为空，将它的右孩子设置为当前节点。(因为中序遍历先左-中-右，现在中是prev，故他的后继就是prev.right)
（3）左子树访问完了：已经访问到了pre.right==cur，也就是我们在b)中设置的步骤，则恢复树的形状，将prev的右孩子重新设为空
（4）访问当前结点cur
（5）遍历右子树

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur, prev = root, None # 从根节点开始遍历
        while cur:
            if not cur.left: # 当前结点没有左孩子
                res.append(cur.val)
                cur = cur.right # 根据中序遍历规则，往下遍历右子树
            else: # 当前节点有左孩子
                prev = cur.left # 按照照中序遍历规则，cur结点的前驱结点是cur的左孩子，故prev=cur.left
                while prev.right and prev.right != cur: # 当pre有右孩子，且pre的右孩子不是我们后来自己添加的那个后继结点cur
                    prev = prev.right # 一直往右找，直到找到左子树上的最右结点
                if not prev.right: # 现在已经找到了左子树上最右侧的叶子结点prev，按照中序遍历规则该节点访问完我们会回撤到cur，访问cur，再访问右子树，因此，将pre的右孩子指向cur
                    prev.right = cur 
                    cur = cur.left # 完成了后继的寻找后按照中序遍历规则继续遍历左子树
                else: # 按道理经过while循环后（line20-21）得到的prev.right都应该是空，若不空，则经过了上面（line22）if的过程，我们给prev重新指定了右孩子
                    # 因此若进入了else部分，说明pre.right==cur,即我们当前结点的左子树已经访问完毕，回到了之前我们手动指定的位置上了
                    prev.right = None # 因此，我们要恢复树的形状（不然就是一个图了），将prev的右孩子重新设为空
                    res.append(cur.val) # 访问当前结点
                    cur = cur.right # 访问当前结点的右子树
        return res
