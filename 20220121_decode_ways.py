# Decode Ways (leetcode)

# Bottom Up Approach (Iteration)
class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, len(dp)):
            prev_char = s[i - 2]
            curr_char = s[i - 1]
            
            if curr_char != '0':
                dp[i] = dp[i - 1]
            
            if 10 <= int(prev_char + curr_char) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[-1]