class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(s):
            mmap={}
            for c in s:
                if not mmap.get(c):
                    mmap[c]=1
                else:
                    mmap[c]+=1
            return mmap
        scount=count(s)
        tcount=count(t)
        if scount==tcount:
            return True
        else:
            return False
x=Solution()
a=x.isAnagram("ra  t","c ar")
print(a)