# Unique Path (leetcode)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize containers
        prev = [1]*n
        curr = [1]*n

        # dp logic
        for i in range(1, m):
            for j in range(1, n):
                curr[j] = curr[j - 1] + prev[j]

                prev = curr
                curr = [1]*n

        return prev[-1]