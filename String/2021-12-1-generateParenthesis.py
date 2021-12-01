# 递归式
class Solution:
    def generateParenthesis(self, n: int):
        res=[]
        # left：左括号有几个
        # right：右括号有几个
        # position：还剩几个位置
        # str：当前括号组合
        def back(left,right,position,str): 
            if position==0: # 当不剩下空位时，即所有位置被填满，则将str加入res
                res.append(str)
            if left>0: # 只要还有左括号，我们就可以选择放一个左括号
                back(left-1,right,position-1,str+'(') # 放了一个左括号后，左括号的数量-1，空位的数量-1，str加上一个左括号
            if right>left: # 如果右括号的数量小于左括号，我们也可以放一个右括号
                back(left,right-1,position-1,str+')')
        
        back(n,n,2*n,'') 
        return res
    
x=Solution()
a=x.generateParenthesis(1)
print(a)
            
            
            