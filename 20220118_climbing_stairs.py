# Climbing Stairs (leetcode)
class Solution:
    def climbStairs(self, n: int) -> int:
        
        # initialize dp array of size n + 1
        dp = [0]*(n + 1)
        
        # initialize base cases: f(0) = 1, f(1) = 1
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            # relation between previous steps and next steps
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
        