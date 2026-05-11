class Solution:
    def maxSubarray(self,nums:list):
        cur=0
        maxi=nums[0]
        for i in range(len(nums)):
            cur+=nums[i]

            maxi=max(maxi,cur)

            if cur<0:
                cur=0
        return maxi
s=Solution()
print(s.maxSubarray([-2,1,-3,4,-1,2,1]))
            
