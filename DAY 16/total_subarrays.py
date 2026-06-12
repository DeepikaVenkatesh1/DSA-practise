class Solution:
    def max_subarray(self,nums,k):
        prefix=0
        seen={0:1}
        count=0
        for i in range(len(nums)):
            prefix+=nums[i]
            seen[prefix]=i

            if (prefix-k) in seen:
                count+=seen[prefix-k]
            
            if prefix in seen:
                seen[prefix]+=1
            else:
                seen[prefix]=1
        return count
sol=Solution()
print(sol.max_subarray([1,-1,5,-2,3],3))
print(sol.max_subarray([1,1,2,1],3))