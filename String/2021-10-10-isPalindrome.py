class Solution:
    def isPalindrome(self, s: str) -> bool:
    # str.isalnum() 所有字符都是数字或者字母
    # str.isalpha() 所有字符都是字母
    # str.isdigit() 所有字符都是数字，如果带小数点，则会返回False
    # str.isspace() 所有字符都是空白字符、t、n、r

        if s.isspace():
            return True
        for i in s:
            if not i.isalnum():
                s=s.replace(i,'')
        if len(s)==0:
            return True
        else:
            s=s.lower()
            p,q=0,len(s)-1
            while p<=q:
                if s[p]==s[q]:
                    p+=1
                    q-=1
                else:
                    return False
            return True
            
            

x=Solution()
a=x.isPalindrome("::::")
print(a)
