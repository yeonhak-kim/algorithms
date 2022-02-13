# Longest Palindromic Substring (leetcode)

# Expand from the center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_length = 0
        
        for i in range(len(s)):
            # odd case
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_length:
                    result = s[l:r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1
                
            # even case
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_length:
                    result = s[l:r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1
        return result