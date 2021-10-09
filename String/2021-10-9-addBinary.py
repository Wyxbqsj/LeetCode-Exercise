# 我们可以借鉴「列竖式」的方法，末尾对齐，逐位相加。在十进制的计算中「逢十进一」，二进制中我们需要「逢二进一」。
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=max(len(a),len(b))
        b=b.zfill(n)
        a=a.zfill(n)
        temp=0
        # dic={'1':1,'0':0}
        
        i=n-1
        res=''
        while i>=0:
            ans=temp+int(a[i])+int(b[i])
            res=res+str(ans%2)
            temp=ans//2
            i=i-1
        if temp:
            res=res+'1'
        res=res[::-1]
        return res

x=Solution()
a=x.addBinary("1010","1011")
print(a)



        
