class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 26进制转10进制
        res=0
        for i in columnTitle:
            res=res*26+ord(i)-65+1  
            #ord(i)-65将字符转成0-25的数字
            #再+1是因为，A-Z对应的是0-25，而题目要求对应着1-26
        return res

x=Solution()
a=x.titleToNumber('AB')
print(a)

        