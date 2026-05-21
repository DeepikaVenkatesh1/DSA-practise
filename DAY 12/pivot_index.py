class Solution:
    def pivotIndex(self,nums):
        prefix=0
        for i in range(len(nums)):
            if prefix==sum(nums[i+1:]):
                return i
            prefix+=nums[i]
        return -1
sol=Solution()
print(sol.pivotIndex([1,7,3,6,5,6]))
