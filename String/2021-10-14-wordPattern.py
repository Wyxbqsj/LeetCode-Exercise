class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def charMap(s,t):
            dic={}
            for i,j in zip(s,t):
                if dic.get(i):
                    if dic[i]==j:
                        continue
                    else:
                        return False
                else:
                    dic[i]=j
            return True
        snew=[]
        b,k=0,0
        while k<len(s):
            if s[k]==' ':
                snew.append(s[b:k])
                k+=1
                b=k
            if k==len(s)-1:
                snew.append(s[b:k+1])
                k=k+1
            else:
                k=k+1
        if len(pattern)!=len(snew):
            return False
        if charMap(pattern,snew) and charMap(snew,pattern):
            return True
        else:
            return False
                
if __name__=="__main__":
    x=Solution()
    a=x.wordPattern("aaa","aa aa aa aa")
    print(a)
          

            
