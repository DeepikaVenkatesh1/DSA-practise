class Solution:
    def maxSumSubarray(self,nums,k):
        left=0
        window=sum(nums[:k])
        maxi=window
        for right in range(k,len(nums)):
            window+=nums[right]-nums[right-k]
            maxi=max(maxi,window)
        return maxi
sol=Solution()
print(sol.maxSumSubarray([1,12,-5,-6,50,3],4))

