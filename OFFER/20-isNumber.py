class Solution:
    def isNumber(self,s:str):
        def isE(c):
            if c=='e' or c=='E':
                return True
            else:
                return False
        
        def isSign(c):
            if c=='+' or c=='-':
                return True
            else:
                return False
        
        s.strip()
        i=0
        while i<len(s):
            if i==0 and (isE(s[i]) or s[i]=='.'):
                return False
            elif i>0:

            