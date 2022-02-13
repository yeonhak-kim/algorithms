# Longest Substring wihtou Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        mapping = {}
        longest_length = 0
        
        for idx in range(len(s)):
            char = s[idx]
            if char in mapping:
                l = max(mapping[char] + 1, l)
                mapping.pop(char)
            
            mapping[char] = r
            longest_length = max(longest_length, r - l + 1)
            r += 1
        
        return longest_length
            
            
        