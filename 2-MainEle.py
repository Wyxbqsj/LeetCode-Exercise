'''
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。
'''

class Solution:
    def majorityElement(self, nums):
        tem=list(set(nums))
        res=-1
        for i in tem:
            if nums.count(i)>len(nums)/2:
                res=i
                break
        return res

x=Solution()
a=x.majorityElement([1,2,5,9,5,9,5,5,5])
print(a)

'''
思路一：摩尔投票法：
哈希表+暴力搜索这种方法无法满足O(1)的空间复杂度，因此需要采用摩尔投票法。
投票法的基本原理是，维护一个众数major和一个频数count，
假设当前数为众数major, 遇到相同的数字则count+1,否则count-1。若前n个票和为0(互相抵消), 则设下一个数为当前数。
最终会发现，如果存在主要元素，那么最终count一定大于0，否则一定不存在主要元素。
但仅大于0也不一定能判断确实存在主要元素，因为如果数组为[4,3,3,2,2,2]，会发现count为2。但是，2并不是主要元素（没有大于一半），所以还要添加验证环节。
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        else:
            count = 0
            major = None
            for i in range(len(nums)): #找到众数
                if count == 0:
                    major = nums[i]
                    count += 1
                else:
                    if nums[i] != major:
                        count -= 1
                    else:
                        count += 1
            if count > 0: #验证环节：判断众数是否大于list长度的一半
                count_identify = 0
                for i in nums:
                    if i == major:
                        count_identify += 1
                        if count_identify > len(nums) / 2:
                            return major
                return -1
            else:
                return -1
'''

'''
思路二：将列表排序，如果存在主要元素，那么排序后，中间那个值一定是主要元素
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1
        else:
            nums.sort()
            mid=len(nums)/2
            if(nums.count(nums[mid])>mid):
                return nums[mid]
            return -1
'''

'''
思路三：使用字典记录数组中值出现的次数，之后遍历字典中的值，若超过数组长度的一半，那这个值就是主要元素
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicts={}
        for i in nums:
            dicts[i]=dicts.get(i,0)+1 #dicts.get(i,0)表示取key==i的value，找不到就返回0
        mid=len(nums)/2
        for i,k in dicts.items(): #i为key,k为value
            if k>mid:
                return i
        return -1
'''
            
