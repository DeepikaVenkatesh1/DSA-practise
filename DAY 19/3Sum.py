class Solution:
    def ThreeSum(self,nums):
        nums.sort()
        res=[]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif s < 0:
                    l+=1
                elif s>0:
                    r-=1
        return res
sol=Solution()
print(sol.ThreeSum([-1,0,1,2,-1,-4]))
                
                
    


    