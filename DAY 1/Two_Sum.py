class Solution:
    def twoSum(self,nums:list,target:int):
        d={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in d:
                return[d[rem],i]
            d[nums[i]]=i

s=Solution()
print(s.twoSum([2,7,11,15],9))

