'''队列法：
先将输入的 digits 中第一个数字对应的每一个字母入队，然后将出队的元素与第二个数字对应的每一个字母组合后入队...直到遍历到 digits 的结尾。
最后队列中的元素就是所求结果。
'''

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        dic={'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','k','l'],
             '6':['m','n','o'],
             '7':['p','q','r','s'],
             '8':['t','u','v'],
             '9':['w','x','y','z']}
        queue=['']
        for digit in digits:
            for _ in range(len(queue)): #一定不能少了这行代码，需要遍历整个队列，将上一轮队列中的字母都pop出来  
                ans=queue.pop(0)
                for i in dic[digit]:
                    queue.append(ans+i)
        return queue
    
x=Solution()
a=x.letterCombinations('23')
print(a)
            
        