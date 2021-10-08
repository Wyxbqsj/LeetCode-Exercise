class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while s[-1]==' ':
            s=s[:-1]

        i=len(s)-1
        length=0
        while i>=0:
            if i==0 and s[0]!=' ':
                return length+1
            if s[i]!=' ':
                i=i-1
                length+=1
            if s[i]==' ':
                return length

x=Solution()
a=x.lengthOfLastWord("luff   yaaa")
print(a)

