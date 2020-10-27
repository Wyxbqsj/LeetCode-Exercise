class Solution:
    def transpose(self, A):
        B=[]
        i=j=0
        for i in range(len(A[i])):
            C=[]
            for j in range(len(A)):
                C.append(A[j][i])
            B.append(C)
        return B

x=Solution()
a=x.transpose([[1,2,3],[4,5,6],[7,8,9]])
print (a) 


'''
优解1：
不调用库函数，一行解决：
class Solution:
    def transpose(self,A):
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
'''

'''
优解2：
矩阵转置本质即翻转行和列，python 内置函数zip 就可以实现
利用 * 号操作符，可以将元组解压为列表。
class Solution:
    def transpose(self,A):
        return zip(*A)
'''

'''
优解3：
暴力求解：一定记得先给B声明大小
class Solution:
    def transpose(self,A):
        B=[[0 for i in range(len(A))] for j in range(len(A[0]))]
        for j in range(len(A[0])):
            for i in range(len(A)):
                B[j][i]=A[i][j]
        return B
'''