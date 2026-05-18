class Solution:
    def maxSumSubarray(self,nums,k):
        window=sum(nums[:k])
        left = 0
        maxi=window
        for i in range(k,len(nums)):
            window+=nums[i]-nums[i-k]
            maxi=max(window,maxi)
        return maxi
sol=Solution()
print(sol.maxSumSubarray([1,12,-5,-6,50,3],4))