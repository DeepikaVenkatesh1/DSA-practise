class Solution:
    def isDuplicate(self,nums):
        seen=set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
sol=Solution()
print(sol.isDuplicate([1,2,3,1]))