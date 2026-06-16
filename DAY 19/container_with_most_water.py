class Solution:
    def containerWithMostWater(self,nums,height):
        left=0
        right=len(nums)-1
        max_area=0
        while left<right:
            width=right-left
            current_area=min(nums[left],nums[right])*width
            max_area=max(max_area,current_area)
            if nums[left]<nums[right]:
                left+=1
            else:
                right-=1
        return max_area
sol=Solution()
print(sol.containerWithMostWater([1,8,6,2,5,4,8,3,7],9))