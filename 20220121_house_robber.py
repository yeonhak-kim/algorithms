# House Robber (leetcode)

# Bottom Up Approach (Iteration)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Case where nums length is 1
        if len(nums) == 1: return nums[0]
        
        # Initialize dp array of size nums ([nums[0] and nums[max(nums[0], nums[1])] are the base cases])
        dp = [nums[0]] + [max(nums[0], nums[1])] + [0]*(len(nums) - 2)
        
        # Main logic
        for idx in range(2, len(nums)):
            dp[idx] = max(dp[idx - 1], nums[idx] + dp[idx - 2])
                
        return dp[-1]