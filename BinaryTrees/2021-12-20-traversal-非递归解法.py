class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

# 非递归解法（参阅文章：https://blog.csdn.net/sgbfblog/article/details/7773103）即迭代解法：本质上是在模拟递归，因为在递归的过程中使用了系统栈，所以在迭代的解法中常用Stack来模拟系统栈。
# 注意栈的先进后出顺序，输出出来的就是倒序打印。
# （1）先序遍历：
'''
算法1：先序遍历非递归访问，使用栈即可实现。先序遍历的非递归访问在所有的遍历中算是最简单的了。
主要思想就是先将根结点压入栈，然后根结点出栈并访问根结点，而后依次将根结点的右孩子、左孩子入栈，直到栈为空为止。
'''
def preOrder(root: TreeNode):
    if not root:
        return None
    stack=[]
    stack.append(root)
    while stack:
        ans=stack[-1]
        stack.pop()
        print(ans.val)
        # 注意栈是先进后出，所以遍历时先访问左子树再访问右子树，因此压入栈时先压右子树再压左子树
        if ans.right:
            stack.append(ans.right)
        if ans.left:
            stack.append(ans.left)
'''
算法2：先序遍历的非递归算法另一算法，也是用的栈，只是稍微复杂点，当左子树遍历完后，需要回溯并遍历右子树。
'''
def preOrder(root: TreeNode):
    stack=[]
    while root or stack:
        if root:
            print(root.val) # 访问结点并入栈
            stack.append(root)
            root=root.left # 一直遍历左子树，直到左子树为空
        else:
            root=stack[-1] # 回溯父亲结点
            stack.pop()
            root=root.right  # 访问右子树    

            
# （2）中序遍历：
'''
中序遍历非递归算法也是采用栈实现，与上面的先序遍历算法2类似，只是访问根结点的时机不同。
'''
def inOrder(root: TreeNode):
    stack=[]
    while root and stack:
        if root:
            stack.append(root) 
            root=root.left  
        else:
            root=stack[-1]  # 将所有的左子树都访问完压入栈后，再访问根结点
            print(root.val)
            stack.pop()
            root=root.right # 访问右子树

# （3）后序遍历
'''
后序遍历的非递归算法较复杂，使用一个栈可以实现，但是过程很繁琐，这里可以巧妙的用两个栈来实现后序遍历的非递归算法。
注意到后序遍历可以看作是下面遍历的逆过程：即先遍历某个结点，然后遍历其右孩子，然后遍历其左孩子。
上面这个过程逆过来就是后序遍历。算法步骤如下：
1.Push根结点到第一个栈s中。
2.从第一个栈s中Pop出一个结点，并将其Push到第二个栈output中。
3.然后Push结点的左孩子和右孩子到第一个栈s中。
4.重复过程2和3直到栈s为空。
5.完成后，所有结点已经Push到栈output中，且按照后序遍历的顺序存放，直接全部Pop出来即是二叉树后序遍历结果。
'''
def postOrder(root: TreeNode):
    if not root:
        return
    stack=[]
    output=[]
    stack.append(root)
    while stack:
        cur=stack[-1]
        output.append(cur)
        stack.pop()
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    
    while output:
        print(output[-1].val)
        output.pop()