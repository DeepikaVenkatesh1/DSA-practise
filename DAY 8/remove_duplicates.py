class Solution:
    def remove_duplicates(self,nums):
        left = 1
        for right in range(1,len(nums)):
            if nums[right]!=nums[right-1]:
                nums[left]=nums[right]
                left+=1
        return left
    

sol=Solution()
nums=[1,1,2]
k=sol.remove_duplicates(nums)
print(nums[:k])


           