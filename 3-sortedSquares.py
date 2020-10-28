'''
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
'''
class Solution:
    def sortedSquares(self, A):
        B=[i*i for i in A]
        B.sort()
        return B

x=Solution()
a=x.sortedSquares([-4,-1,0,3,10])
print(a)

'''
思路二：实际上，我们也可以利用双指针的技巧。
用两个指针记录首尾。
将平方大的插入到数组末尾，然后继续移动小的指针
重复步骤二，直到两个指针相遇并超越
class Solution:
    def sortedSquares(self, A):
        ans  = []
        l, r = 0, len(A) - 1
        while l <= r:
            if abs(A[l]) > abs(A[r]):
                ans.insert(0, A[l] ** 2)
                l += 1
            else:
                ans.insert(0, A[r] ** 2)
                r -= 1     
        return ans
!!!注意到 insert 的操作（这里指的是往数组前面插入值）时间复杂度为 O(N)，因此总的时间复杂度会是 N^2。比上面排序的算法还要差。但是实际上，我们没必须用 insert。
因为 ans 的长度是已知的，因此可以使用一个变量记录插入的索引即可，利用数组可以随机访问的特性， 时间复杂度可以降低到 O(N)。 可见，基础的数据结构知识对算法的帮助有多大。
改进后：
class Solution:
    def sortedSquares(self, A):
        ans = [0] * len(A)
        l, r, cur = 0, len(A) - 1, len(A) - 1
        while l <= r:
            if abs(A[l]) > abs(A[r]):
                ans[cur] = A[l] ** 2
                l += 1
            else:
                ans[cur] = A[r] ** 2
                r -= 1
            cur -= 1
        return ans
'''
        