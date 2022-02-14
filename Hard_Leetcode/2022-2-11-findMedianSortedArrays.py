
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        mid_index=(m+n)//2
        count=0
        i,j=0,0
        new=[]
        while count<=mid_index:
            if i>=m and j>=n:
                break
            if i>=m:
                new.append(nums2[j])
                j+=1
            if j>=n:
                new.append(nums1[i])
                i+=1
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i+=1
            else:
                new.append(nums2[j])
                j+=1
            count+=1
        if (m+n)%2==0:
            return (new[mid_index-1]+new[mid_index])/2
        return new[mid_index]
        
                
                
                