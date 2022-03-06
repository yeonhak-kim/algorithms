# Unique Binary Search Trees

# Dynamic Programming
class Solution:
    def numTrees(self, n: int) -> int:
        # [LEFT, I-TH, RIGHT]
        # -> LEFT-SUB-PROBLEM * RIGHT-SUB-PROBLEM
        dp = [1] + [1] + [0]*(n - 1)
    
        for k in range(2, n + 1):
            for i in range(1, k + 1):
                dp[k] += dp[i - 1]*dp[k - i]
        
        return dp[-1]
        