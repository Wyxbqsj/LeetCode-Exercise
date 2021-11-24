# class Solution:
# 二维数组暴力解法，跑不出来
#     def convert(self, s:str, numRows:int)->str:
#         store=[[None for i in range(len(s))] for j in range(numRows)]
#         i=0
#         count=0
#         while i<len(s):
#             if i+numRows<len(s):
#                 win=s[i:i+numRows]
#                 count+=1
#                 if count%2!=0:
#                     for k in range(numRows):
#                         store[k][i]=win[k]
#                 else:
#                     l=i
#                     for k in range(-1,numRows):
#                         store[k][l]=win[k]
#                         l+=1
#                 i=i+numRows-1
#         res=''
#         i,j=0,0
#         for i in range(len(store)):
#             for j in range(len(store[i])):
#                 if store[i][j]!=None:
#                     res+=store[i][j]
#         return res
      
              
# 从左到右迭代s，将每个字符添加到合适的行。可以使用当前行i和当前方向flag这两个变量对合适的行进行跟踪。
# 只有当我们向上移动到最上面的行i=0或向下移动到最下面的行i=numRows-1时，当前方向才会发生改变。                  
class Solution:
     def convert(self, s:str, numRows:int)->str:
         if numRows==1:
             return s
         res=['' for _ in range(numRows)]
         i,flag=0,-1
         for c in s:
             res[i]+=c
             if i==0 or i==numRows-1: 
                 flag=-flag
             i=i+flag
         return ''.join(res)
             
             







