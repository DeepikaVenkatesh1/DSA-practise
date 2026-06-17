class Solution:
    def set_miss_match(self,nums):
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1

            duplicate=-1
            missing=-1

            for num in range(1,len(nums)+1):
                if freq.get(num,0)==2:
                    duplicate=num
                if freq.get(num,0)==0:
                    missing=num
        return [duplicate,missing]
    
sol=Solution()
print(sol.set_miss_match([1,2,2,4]))
