class Solution:
    def removeDuplicates(self,nums):
        left=0
        for i in range(1,len(nums)):
            if nums[left]!=nums[i]:
                left+=1
                nums[left]=nums[i]
        return left+1
sol=Solution()
print(sol.removeDuplicates([1,1,2,3,3,4]))