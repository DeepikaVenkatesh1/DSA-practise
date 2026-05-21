class Solution:
    def twoSum(self,nums,target):
        dict={}
        for i,num in enumerate(nums):
            need=target-num
            if need in dict:
                return [dict[need],i]
            dict[num]=i
sol=Solution()
print(sol.twoSum([2,7,11,15],9))
            