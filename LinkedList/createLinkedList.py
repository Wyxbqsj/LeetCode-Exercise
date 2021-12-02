# 单向链表结点
class Node:
    # 每个结点存储两个信息，数据和指向下一个结点的指针
    def __init__(self,value=None,next=None) -> None:
        self.value=value
        self.next=next

# 双向链表结点
class Node2:
    def __init__(self,value=None,next=None,pre=None) -> None:
        self.value=value
        self.next=next
        self.pre=pre
        
# 向链表中插入数据
def insertNode(i,p): #插入一个结点值为i，其前驱结点为p
    node=Node() #新建一个空结点，下一步要将这个结点插入到链表中
    node.value=i
    node.next=p.next
    p.next=node   
    
#将一个list转成一个链表
def createLinkedList(linkedList,normalList,i): #传入普通的list，返回链表 
    if i<len(normalList):
        if normalList[i]==None: #若普通list中的所有元素都已经转换完成
            return linkedList
        else:
            linkedList=Node(normalList[i])
            linkedList.next=createLinkedList(linkedList.next,normalList,i+1) # next是一个子链表
            return linkedList
    return linkedList

# 定义链表
# 链表需要首地址指针head
class SingleLinkList():
    def __init__(self) -> None:
        self.head=None
        
    def __init__(self,head=None) -> None: #两种完全等价的写法
        self.head=head
# 创建链表
if __name__=='__mian__':
    link_list=SingleLinkList()
    node1=Node(1)
    node2=Node(2)
    link_list.head=node1
    node1.next=node2
    
    print(link_list.head.value)
    print(link_list.head.next.value)

