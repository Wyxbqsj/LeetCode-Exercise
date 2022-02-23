# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo,hi=1,n
        while lo<hi:
            mid=lo+(hi-lo)//2 # 注意当lo和hi都是很大的int数据时，用(lo+hi)//2求mid，可能会溢出
            if isBadVersion(mid):
                hi=mid
            else:
                lo=mid+1
        return lo