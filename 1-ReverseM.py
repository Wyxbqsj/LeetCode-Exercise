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