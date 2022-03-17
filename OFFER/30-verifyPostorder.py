# 题目：剑指 Offer 33. 二叉搜索树的后序遍历序列，https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/

# 方法一：递归写法
class Solution:
    def verifyPostorder(self,postorder):
        def recur(begin,end):
            if begin>=end: # 递归出口：若树没有或只有一个结点，则返回True
                return True
            p=begin # 遍历指针初始化为起始点
            while postorder[p]<postorder[end]: # 找第一个大于root的结点，即为右子树开始的位置
                p+=1
            # 经过上面的遍历也已经知道rightBegin之前，也就是左子树都是小于根节点的，即左子树已经得到判断
            rightBegin=p
            while postorder[p]>postorder[end]: # 判断右子树是否都大于根节点
            # 上面的while循环一定不能有等于号，否则遍历到了终点，p==end，则陷入了死循环
                p+=1
            # 若跳出循环时，p还未遍历到右子树的末尾，即p!=end就跳出了，则该树的右子树存在一个结点值要与root，不满足BST
            return p==end and recur(begin,rightBegin-1) and recur(rightBegin,end-1)
        
        return recur(0,len(postorder)-1)


x=Solution()
a=x.verifyPostorder([1,3,2,6,5])
print(a)
            
            
