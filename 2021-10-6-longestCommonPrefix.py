#字符串第2题
class Solution:
    def longestCommonPrefix(self, strs):
        mins=strs[0]
        min=len(mins)
        for s in strs:
            if len(s)<min:
                min=len(s)
                mins=s
        i=0
        while i<len(strs):
            if strs[i][0:min]==mins:
                i=i+1
            else:
                mins=mins[:-1]
                min=min-1
                if min==0:
                    break
        return mins

x=Solution()
a=x.longestCommonPrefix(["dog","racecar","car"])
print(a)
        

