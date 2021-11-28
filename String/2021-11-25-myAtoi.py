import math
class Solution:
    def myAtoi(self, s: str) -> int:
        # strip()：删除字符串前后（左右两侧）的空格或特殊字符。
        # lstrip()：删除字符串前面（左边）的空格或特殊字符。
        # rstrip()：删除字符串后面（右边）的空格或特殊字符。
        def left(str,i):
            news=''
            while i<len(str) and str[i].isdigit():
                news=news+str[i]
                i=i+1
            length=len(news)
            num=0
            j=length-1
            while j>=0:
                num=num+int(news[j])*math.pow(10,length-1-j)
                j=j-1
            return num
        flag=1
        k=0
        if len(s)==0:
            return 0
        while s[k]==' ':
            k=k+1
        if k==len(s):
            return 0
        if s[k]=='-':
            flag=-1
            k=k+1
            num=left(s,k)
        elif s[k]=='+':
            k=k+1
            num=left(s,k)
        else:
            num=left(s,k)
        
        num=num*flag
        if num<math.pow(-2,31):
            return int(math.pow(-2,31))
        elif num>math.pow(2,31)-1:
            return int(math.pow(2,31)-1)
        else:
            return int(num)


x=Solution()
a=x.myAtoi("-+42")    
print(a)   
                