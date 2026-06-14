class Solution:
    def longestSubstring(self, s, k):
        freq = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


sol = Solution()
print(sol.longestSubstring("eceba", 2)) 
print(sol.longestSubstring("aa", 1))     