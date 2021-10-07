#字符串练习第1题
class Solution:
    def romanToInt(self, s):
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        res=0
        while i<len(s):
            if i+1<len(s) and dic[s[i]]<dic[s[i+1]]:
                ans=dic[s[i+1]]-dic[s[i]]
                res=res+ans
                i=i+2
            else:
                res=res+dic[s[i]]
                i=i+1
        return res


x=Solution()
a=x.romanToInt('IV')
print(a)