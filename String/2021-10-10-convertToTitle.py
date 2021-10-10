# 这是一道从1开始的26进制转换题。
# 对于一般性的进制转换题目，只需要不断地对 columnNumbercolumnNumber 进行 % 运算取得最后一位，然后对 columnNumber 进行 / 运算，将已经取得的位数去掉，直到 columnNumber为 0即可。
# 一般性的进制转换题目无须进行额外操作，是因为我们是在「每一位数值范围在 [0,x)」的前提下进行「逢 x进一」。
# 但本题需要我们将从 1 开始，因此在执行「进制转换」操作前，我们需要先对 columnNumber 执行减一操作，从而实现整体偏移。


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic={1:'A', 2:'B', 3:'C',4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J',
            11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T',
            21:'U', 22:'V', 23:'W', 24:'X', 25:'Y',26:'Z'}
        i=-1
        res=''
        while columnNumber>0:
            columnNumber-=1
            i=columnNumber%26
            res=res+dic[i+1]
            columnNumber=columnNumber//26
        res=res[::-1]
        return res

x=Solution()
a=x.convertToTitle(702)
print(a)