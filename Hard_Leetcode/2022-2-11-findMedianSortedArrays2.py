from typing import List
# 时间复杂度为O(log(m+n))的方法：第k小的数的变种
# 如果对时间复杂度的要求有 log，通常都需要用到二分查找
'''
题解：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
根据中位数的定义，当 m+n 是奇数时，中位数是两个有序数组中的第 (m+n)/2 个元素
当 m+n 是偶数时，中位数是两个有序数组中的第 (m+n)/2(m+n)/2 个元素和第 (m+n)/2+1个元素的平均值
因此，这道题可以转化成寻找两个有序数组中的第 k小的数，其中 k 为 (m+n)/2 或 (m+n)/2+1。

具体思路：
假设两个有序数组分别是A和B。要找到第 k 个元素，我们可以比较 A[k/2−1] 和B[k/2−1]，其中 / 表示整数除法。
由于 A[k/2−1] 和 B[k/2−1] 的前面分别有 A[0..k/2−2] 和 B[0..k/2−2]，即 k/2−1 个元素，
对于A[k/2−1] 和 B[k/2−1] 中的较小值，最多只会有 (k/2−1)+(k/2−1)≤k−2 个元素比它小，那么它就不能是第 k 小的数了，最多是第k-1小的数。
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(A,B,k):
            if k==1:
                return min(A[0],B[0])
            la=len(A)
            lb=len(B)
            if la==0:
                return B[k-1]
            elif lb==0:
                return A[k-1]
            index=min(la-1,lb-1,k//2-1)
            if A[index]<B[index]:
                return findKth(A[index+1:],B,k-index)
            else:
                return findKth(A,B[index+1:],k-index)
            
        m=len(nums1)
        n=len(nums2)
        k=(m+n)//2
        x=findKth(nums1,nums2,k)
        if (m+n)%2==0:
            y=findKth(nums1,nums2,k-1)
            return (x+y)/2
        return x
        