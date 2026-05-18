class Solution:
    def longestSubstring(self,s):
        left = 0
        right = 0
        char_set=set()
        maxi=0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            maxi=max(maxi,right-left+1)
        return maxi
sol=Solution()
print(sol.longestSubstring("abcabcbb"))
    
