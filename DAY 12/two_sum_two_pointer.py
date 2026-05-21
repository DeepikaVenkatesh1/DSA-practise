class Solution:
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return left,right
            elif total < target:
                left += 1
            else:
                right-=1
sol=Solution()
print(sol.twoSum([1,2,2,3,4,4,5],9))