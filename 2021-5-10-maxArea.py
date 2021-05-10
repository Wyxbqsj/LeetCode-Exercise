'''2021-5-10-maxArea.py
题目：盛水最多的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水
'''

#思路：双指针
class Solution:
    def maxArea(self, height):
        l=0
        r=len(height)-1
        maxRes=(r-l)*min(height[l],height[r])
        while l<r:
            if height[l]<=height[r]:
                l=l+1
                ans=(r-l)*min(height[l],height[r])
                if maxRes<ans:
                    maxRes=ans
            else:
                r=r-1
                ans=(r-l)*min(height[l],height[r])
                if maxRes<ans:
                    maxRes=ans
        return maxRes

x=Solution()
a=x.maxArea([1,1])
print(a)
#缺点：代码冗余很多——比如(r-l)*min(height[l],height[r])写了很多遍
#改进代码：
class Solution:
    def maxArea(self, height):
        l=0
        r=len(height)-1
        maxRes=0
        while l<r:
            ans=(r-l)*min(height[l],height[r])
            maxRes=max(ans,maxRes)
            if height[l]<=height[r]:
                l=l+1
            else:
                r=r-1
        return maxRes