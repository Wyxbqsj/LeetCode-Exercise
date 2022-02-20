class Solution:
    def reverseWords(self,str):
        begin,i=0,0
        ans=[]
        for i in range(len(str)):
            if str[i]==' ':
                ans.append(str[begin:i])
                begin=i+1
        ans.append(str[begin:i+1])
        str=''
        for s in range(len(ans)-1,-1,-1):
            str=str+ans[s]+' '
        return str[:-1]     

x=Solution()
a=x.reverseWords("the sky is blue")
print(a)             
            