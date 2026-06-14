class Solution:
    def xorTotalSubarrays(self,nums,k):
        xor_prefix=0
        seen={0:1}
        count=0
        for i in range(len(nums)):
            xor_prefix^=nums[i]
            need=xor_prefix^k
            count+=seen.get(need,0)
            seen[xor_prefix]=seen.get(xor_prefix,0)+1
        return count
sol=Solution()
print(sol.xorTotalSubarrays([1,1,1],2))