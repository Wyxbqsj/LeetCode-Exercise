# 题目：剑指 Offer 35. 复杂链表的复制，https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

'''方法一：哈希表,时间复杂度O(N),空间复杂度O(N)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return # 一定要有这一步，key不能为None
        dic={} # key是原链表结点，value是新链表结点
        cur=head
        while cur: # 先将结点全部加入到哈希表dic中，后面再构建next和random关系
            dic[cur]=Node(cur.val) # key是cur，value是创建的新节点Node(cur.val)
            cur=cur.next
        cur=head
        while cur: # dic[cur]是新链表的结点，get()函数传入key，返回value
            dic[cur].next=dic.get(cur.next) # 新链表结点的next是，新链表创建出来的新结点Node(cur.next.val)，而不能直接写成dic[cur].next=cur.next，这样的话就是新链表指向原链表了，完全乱套
            dic[cur].random=dic.get(cur.random)
            cur=cur.next
        return dic[head]
'''


# 方法二：拼接+拆分，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        # 拼接链表
        cur=head
        while cur:
            tmp=Node(cur.val)
            tmp.next=cur.next
            cur.next=tmp
            cur=cur.next.next
        
        # 设置random
        cur=head
        while cur:
            if cur.random: # 注意不要漏写了这个判断
                cur.next.random=cur.random.next # cur是原结点，cur.next代表新结点；所以这句话的意思是新结点的random指向原结点random的next，即我们所添加的新结点
            cur=cur.next.next
            # 在拼接链表时，我们只设置了新链表的next，他们的random都默认为None，因此当不满足这个if判断句时，random不发生修改，保持为None, cur遍历到下一个节点
        
        # 拆分链表
        cur,res=head.next,head.next
        pre=head
        while cur.next:
            # 一定是先修改pre.next再修改cur.next，不然会乱套，可以画图感受
            pre.next=pre.next.next
            cur.next=cur.next.next
            pre=pre.next
            cur=cur.next
        pre.next=None # 单独处理原链表尾结点，不然的话pre.next指向的是新链表的尾结点，那么他们还没有完全分开
        return res
            
