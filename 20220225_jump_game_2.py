# Jump Game 2 (leetcode)

# Greedy Approach
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        
        next_location = 0
        jump_count = 0
        end_of_current_jump = 0
        
        for curr in range(N - 1):
            if end_of_current_jump == N - 1:
                break 
            
            max_jump = min(curr + nums[curr], N - 1)
            next_location = max(next_location, max_jump)
            
            if curr == end_of_current_jump:
                jump_count += 1
                end_of_current_jump = next_location
        
        return jump_count