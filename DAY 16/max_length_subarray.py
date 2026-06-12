class Solution:
    def max_subarray(self,nums,k):
        prefix=0
        seen={}
        max_len=0
        for i in range(len(nums)):
            prefix+=nums[i]
            seen[prefix]=i

            if prefix==k:
                max_len=max(max_len,i+1)
            
            if (prefix-k) in seen:
                max_len=max(max_len,i-seen[prefix-k])
        return max_len
sol=Solution()
print(sol.max_subarray([1,-1,5,-2,3],3))
print(sol.max_subarray([1,1,2,1],3))