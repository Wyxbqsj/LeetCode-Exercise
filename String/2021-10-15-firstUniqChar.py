from typing import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=Counter(s)
        for i in s:
            if l[i]==1:
                return s.index(i)
        return -1


x=Solution()
a=x.firstUniqChar("loveleetcode")
print(a)
