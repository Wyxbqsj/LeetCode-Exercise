'''根据罗马数字的唯一表示法，为了表示一个给定的整数num，我们寻找不超过num 的最大符号值，
将num 减去该符号值，然后继续寻找不超过num 的最大符号值，将该符号拼接在上一个找到的符号之后，循环直至num 为 0。最后得到的字符串即为num 的罗马数字表示。'''
class Solution:
    def intToRoman(self, num: int) -> str:
        dic={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',
             50:'L',90:'XC',100:'C',400:'CD',500:'D',
             900:'CM',1000:'M'}
        l=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        res=''
        i=len(l)-1
        while i>=0 and num!=0:
            if num>=l[i]:
                res+=dic[l[i]]
                num-=l[i]
            else:
                i=i-1
        return res

x=Solution()
a=x.intToRoman(3999)
print(a)
                
            
            
            