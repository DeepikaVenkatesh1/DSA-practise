class Solution:
    def kadanes(self,nums):
        cur = 0
        maxi=0
        for n in nums:
            cur+=n
            maxi=max(maxi,cur)
            if n<0:
                cur=0
        return maxi
print(Solution().kadanes([-2,1,-3,4,-1,2,1,-5,4]))