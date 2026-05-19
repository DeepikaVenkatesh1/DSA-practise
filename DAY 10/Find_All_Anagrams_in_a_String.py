from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        p_count = Counter(p)
        left = 0
        result = []
        window = Counter()

        for right in range(len(s)):
            window[s[right]] += 1

            # shrink window
            if right - left + 1 > len(p):
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # compare maps
            if window == p_count:
                result.append(left)

        return result


sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
sol=Solution()
print(sol.findAnagrams("cbaebabacd","abc"))

