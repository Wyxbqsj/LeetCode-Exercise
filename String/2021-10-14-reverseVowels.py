class Solution:
    def reverseVowels(self, s: str) -> str:
        dic={'a':1,'e':2,'i':3,'o':4,'u':5,'A':1,'E':1,'I':1,'O':1,'U':1}
        s=list(s)
        i,j=0,len(s)-1
        while i<j:
            if dic.get(s[i]) and dic.get(s[j]):
                t=s[i]
                s[i]=s[j]
                s[j]=t
                i+=1
                j-=1
            if not dic.get(s[j]):
                j-=1   
            if not dic.get(s[i]):
                i+=1  
        return ''.join(s)

if __name__=="__main__":
    x=Solution()
    a=x.reverseVowels("etcode")
    print(a)

               
