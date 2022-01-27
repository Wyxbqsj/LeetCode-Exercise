from typing import List
# 把杨辉三角所有行都枚举出来，返回最后一行的结果
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==1:
            return [1,1]       
        
        f=[]
        for x in range(rowIndex+1):
            dp=[1 for _ in range(x+1)]
            f.append(dp)
        
        for i in range(2,rowIndex+1):
            for j in range(i+1):
                if j!=0 and j!=i:
                    f[i][j]=f[i-1][j-1]+f[i-1][j]
        return f[rowIndex]


'''复杂度更低的做法：
用一个list来存放答案，循环rowIndex次，每次都先在列表后方添加一个1
然后从第二个数开始，把自己和前面的数相加。
为了确保下一个数可以和当前数相加，用一个temp来暂存未改变前的数字
循环到底返回res即可

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res.append(1) # 保证了最后一位是1
            for j in range(1, len(res) - 1):
                if j == 1:
                    temp = res[j]
                    res[j] = res[j] + 1
                else:
                    tempHere = res[j]
                    res[j] = res[j] + temp
                    temp = tempHere
        return ret
'''
  