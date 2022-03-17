# 题目：剑指 Offer 17. 打印从1到最大的n位数，https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
'''方法一：弱智解法：
class Solution:
    def printNumber(self,n):
        def judge(x):
            count=0
            while x:
                count+=1
                x=x//10
            return count<=n
        res=[]
        i=1
        while True:
            if not judge(i):
                break
            res.append(i)
            i+=1
        return res
'''

# 方法二：大数解法，分治法（全排列），解析：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
# 全排列后需要（1）删除高位0；（2）题目要求从数字1开始print，而非0
class Solution:
    def printNumber(self,n):
        def DFS(x): # 固定第x位
            if x==n:
                s=''.join(nums[self.start:]) # start之前都是0
                if s!='0': # 数字从1开始，所以我们删掉0
                    res.append(s)
                if n-self.start==self.nine: # 所有位都位9时，高位多余的0减少一个，故start-1
                    self.start-=1
                return
            
            for i in range(10): # 在x个位置递归放进0-9
                if i==9:
                    self.nine+=1
                nums[x]=str(i)
                DFS(x+1) # x位固定好了开始固定x+1位
            self.nine-=1 # 在回溯前恢复nine
        
        res=[]
        nums=[0]*n # 初始化每个数字，n个位置上都是0
        self.nine=0 # 开始数字中9的个数都是0
        self.start=n-1 # 字符串的左边界开始在n-1,表示前n-1个0都会被删掉，来保证添加的数字字符串nums[start:]中无高位多余的0
        DFS(0)
        return ','.join(res)

x=Solution()
a=x.printNumber(3)
print(a)                             
            