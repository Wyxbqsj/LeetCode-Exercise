class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        elif len(haystack)==0 or len(haystack)<len(needle):
            return -1
        else:
            i=0
            while i<len(haystack)-len(needle)+1:
                if haystack[i:i+len(needle)]==needle:
                    return i
                else:
                    i+=1
            if i==len(haystack)-len(needle)+1:
                return -1
            # i=0
            # j=0
            # count=0
            # while i<len(haystack):
            #     if j==len(needle):
            #         break 
            #     if haystack[i]==needle[j]: 
            #         i=i+1
            #         j=j+1
            #         print(i,j)
            #     else:
            #         i=i+1
            #         j=0
            # if j==0:
            #     return -1
            # if j==len(needle):
            #     return i-count
x=Solution()
a=x.strStr("abb","abaaa")
print(a)