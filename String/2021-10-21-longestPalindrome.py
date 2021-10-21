class Solution:
    # 中心扩展算法
    # 枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止，此时的回文串长度即为此「回文中心」下的最长回文串长度。我们对所有的长度求出最大值，即可得到最终的答案
    
    def expend(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return left+1,right-1
    
    # 注意是从边界情况不断向外扩展，而不是从回文中心开始向外扩展直到达到边界情况
    def longestPalindrome(self, s: str) -> str:
        start,end=0,0
        for i in range(len(s)):
            left1, right1=self.expend(s, i, i) # 第一种边界情况，只有一个字母，一定是回文串
            left2, right2=self.expend(s, i, i+1) # 第二种边界情况，有两个字母，当且仅当他们相等时才是回文串，可以向外扩展
            # start 和 end用来记录最长的回文串的长度
            if right1-left1>end-start:
                start, end=left1, right1
            if right2-left2>end-start:
                start, end=left2, right2
        return s[start:end+1]
        
