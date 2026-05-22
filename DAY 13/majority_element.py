class Solution:
    def majorityElement(self,nums):
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num]>len(nums)//2:
                return num
        return -1
print(Solution().majorityElement([2,2,1,1,1,2,2]))