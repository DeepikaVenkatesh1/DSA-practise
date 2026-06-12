class Solution:
    def total_subarrays(self, nums, k):
        prefix = 0
        count = 0
        seen = {0: 1}

        for i in range(len(nums)):
            prefix += nums[i]

            count += seen.get(prefix - k, 0)

            seen[prefix] = seen.get(prefix, 0) + 1

        return count
sol = Solution()
print(sol.total_subarrays([1, 1, 1], 2))