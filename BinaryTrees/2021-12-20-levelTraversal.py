class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right
        
# 中序前序后序都是深度优先DFS，可以递归实现。层次遍历是广度优先BFS，用队列实现。
# 深度遍历DFS的运行过程是先进后出的，自然的方法是栈和递归
# 广度遍历BFS的运行过程是先进先出的，自然的方法是队列

'''
参阅文章：https://blog.csdn.net/sgbfblog/article/details/7773103
如果不考虑分层换行打印，则用一个队列可以很容易的通过非递归实现层序遍历。但是要每打印一层换一行，就显得稍微复杂了一点。
可以有两种方法，第一种使用两个队列，代码很简练，第二种方法则是使用一个队列，代码稍显复杂。
'''

# 方法一：使用两个队列
'''
第一个队列currentLevel用于存储当前层的结点，第二个队列nextLevel用于存储下一层的结点。
当前层currentLevel为空时，表示这一层已经遍历完成，可以打印换行符了。
然后将第一个空的队列currentLevel与队列nextLevel交换，然后重复该过程直到结束。这个算法比较好理解。
'''
# from queue import Queue
import queue
# Python中的队列模块queue详解见链接：https://www.cnblogs.com/itogo/p/5635629.html或https://blog.csdn.net/brucewong0516/article/details/84025027
# 队列类似于一条管道，元素先进先出,进put(arg)，取get( )。put(item,[]): 将item放入队列中；get(): 从队列中移除并返回一个数据
# 需要注意的是：队列都是在内存中操作，进程退出，队列清空，另外，队列也是一个阻塞的形态。
def levelOrder1(root: TreeNode):
    if not root:
        return
    currentLevel=queue.Queue()
    nextLevel=queue.Queue()
    while currentLevel:
        cur=currentLevel.get()
        if cur: # currentLevel中只要有元素就一直访问
            print(cur.val)
            # 将cur结点的孩子们加入到下一层的队列中
            nextLevel.put(cur.left)
            nextLevel.put(cur.right)
        if currentLevel.empty(): # 当前层遍历完了，转移到下一层
            swap(currentLevel,nextLevel)

def swap(cur:queue, next:queue): # 将next队列中的node，全部put到cur队列中
    while not next.Empty():
        node=next.get()
        cur.put(node)
        
        

# 方法二：使用一个队列
# 只使用一个队列的话，需要额外的两个变量来保存当前层结点数目以及下一层的结点数目。
def levelOrder2(root:TreeNode):
    if not root:
        return
    q=queue.Queue()
    curNodeNumber=1 # 保存当前层结点数目
    nextNodeNumber=0 # 保存下一层结点数目
    q.put(root)
    while not q.empty():
        cur=q.get()
        curNodeNumber-=1
        if cur:
            print(cur.val)
            q.put(cur.left)
            q.put(cur.right)
            nextNodeNumber+=2
        if curNodeNumber==0:
            curNodeNumber=nextNodeNumber
            nextNodeNumber=0
        
    
