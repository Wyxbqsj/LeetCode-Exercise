class Solution:
    def fourSum(self, nums, target):
        if len(nums)<4:
            return []
        else:
            nums.sort()
            res=list()
            for a in range(len(nums)):
                if a>0 and nums[a]==nums[a-1]:
                    continue
                for b in range(a+1,len(nums)):
                    if b>a+1 and nums[b]==nums[b-1]:
                        continue
                    
                    d=len(nums)-1
                    for c in range(b+1,len(nums)):
                        if c>b+1 and nums[c]==nums[c-1]:
                            continue
                        while c<d and nums[a]+nums[b]+nums[c]+nums[d]>target:
                            d=d-1
                        if c==d:
                            break
                        if nums[a]+nums[b]+nums[c]+nums[d]==target:
                            res.append([nums[a],nums[b],nums[c],nums[d]])
            return res

x=Solution()
a=x.fourSum([1,0,-1,0,-2,2],0)
print(a)
