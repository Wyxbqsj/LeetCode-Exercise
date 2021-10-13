# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归实现深度优先搜索
# 最直观的方法是使用深度优先搜索。在深度优先搜索遍历二叉树时，我们需要考虑当前的节点以及它的孩子节点。
# 如果当前节点不是叶子节点，则在当前的路径末尾添加该节点，并继续递归遍历该节点的每一个孩子节点。
# 如果当前节点是叶子节点，则在当前路径末尾添加该节点后我们就得到了一条从根节点到叶子节点的路径，将该路径加入到答案即可。
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def listcreateTree(rootClass,rootList,i):
    if i<len(rootList):
        if rootList[i]==None:
            return None
        else:
            rootClass=TreeNode(rootList[i])
            rootClass.left=listcreateTree(rootClass.left,rootList,2*i+1)
            rootClass.right=listcreateTree(rootClass.right,rootList,2*i+2)
            return rootClass
    return rootClass


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths=[]
        def searchPath(root,path):
            if root:
                path+=str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path+='->'
                    searchPath(root.left,path)
                    searchPath(root.right,path)
        searchPath(root,'')
        return paths

if __name__=="__main__":
    x=Solution()
    tree=TreeNode(0) #初始化一个tree
    tree=listcreateTree(tree,[1,2,3,None,5],0)
    a=x.binaryTreePaths(tree)
    print(a)

            
        
