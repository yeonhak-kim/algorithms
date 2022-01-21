# House Robber 2 (leetcode)

# Bottom Up Approach (Iteration: 1 pass)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Case where nums is size 1
        if len(nums) == 1: return nums[0]
        
        # Case where nums is size 2
        if len(nums) == 2: return max(nums[0], nums[1])
        
        # Initialize 2 dp arrays
        # dp1 = start from index 0 and ends at index n - 1
        # dp2 = start from index 1 and ends at index n
        dp1 = [nums[0]] + [max(nums[0], nums[1])] + [0]*(len(nums) - 3)
        dp2 = [nums[1]] + [max(nums[1], nums[2])] + [0]*(len(nums) - 3)
        
        # Initalize pointer
        n = 2
        # Main logic
        while n < len(nums) - 1: 
            dp1[n] = max(dp1[n - 1], nums[n] + dp1[n - 2])
            dp2[n] = max(dp2[n - 1], nums[n + 1] + dp2[n - 2])
            n += 1
        
        return max(dp1[-1], dp2[-1])