from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        l=Counter(s)
        res=0
        mark=False
        for i in l.values():
            temp=i%2
            ans=i//2
            res=res+ans*2
            if temp==1:
                mark=True
        if mark:
            res+=1
        return res

x=Solution()
a=x.longestPalindrome("Cc")
print(a)
