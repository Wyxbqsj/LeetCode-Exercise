class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n=max(len(num1),len(num2))
        num1=num1.zfill(n)
        num2=num2.zfill(n)
        carry=0
        res=[]
        for i in range(n-1,-1,-1):
            temp=ord(num1[i])-48+ord(num2[i])-48+carry
            res.append(temp%10)
            carry=temp//10
        if carry:
            res.append(carry)
        res=res[::-1] 
        ans=''
        for i in res:
            ans+=str(i)
        return ans

x=Solution()
a=x.addStrings('1','9')
print(a)


