class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic={}
        for i in magazine:
            if dic.get(i):
                dic[i]+=1
            else:
                dic[i]=1
      
        for s in ransomNote:
            if not dic.get(s):
                return False
            elif dic[s]==0:
                return False
            else:
                dic[s]-=1
        return True

if __name__=="__main__":
    x=Solution()
    a=x.canConstruct("aaca","baca")
    print(a)


