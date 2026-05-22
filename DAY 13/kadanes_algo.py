class Solution:
    def kadanes(self,nums):
        cur = 0
        maxi = nums[0]
        for n in nums:
            cur+=n
            maxi=max(cur,maxi)
            if cur<0:
                cur=0
        return maxi
sol=Solution()
print(sol.kadanes([-2,1,-3,4,-1,2,1,-5,4]))
