INT_MAX=2**31-1
INT_MIN=-2**31

class Solution:
    def myAtoi(self, s:str)->int:
        res=0
        i=0
        flag=1
        lens=len(s)
        while i<lens and s[i]==' ':
            i=i+1
        start=i
        while i<lens:
            c=s[i]
            if start==i and c=="+": #加一个start变量即可控制除空格外的第一个字符到底是什么
                flag=1
                i=i+1
            elif start==i and c=='-':
                flag=-1
                i=i+1
            elif c.isdigit():
                num=int(c)
                res=res*10+num
                i=i+1
            else:
                break
        res=res*flag
        if res>=INT_MAX/10:
            return INT_MAX
        if res<=INT_MIN/10:
            return INT_MIN
        else:
            return res

x=Solution()
a=x.myAtoi("-+42")    
print(a)             
        
