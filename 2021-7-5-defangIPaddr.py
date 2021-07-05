#将字符串中的"."换成"[.]"
#方法1-直接用replace函数
'''
class Solution:
    def defangIPaddr(self, address):
        return address.replace('.','[.]')
'''

#方法2：遇到就替换，没有就保持原样，注意字符串中替换赋值不能再直接用等号了，要学会利用加号
class Solution:
    def defangIPaddr(self, address):
        ans=''
        for c in address:
            if c==".":
                ans=ans+"[.]"
            else:
                ans=ans+c
        return ans
x=Solution()
var='1.1.1.1'
a=x.defangIPaddr(var)
print (a)