# Leetcode Daily Challenge
# September 01: Array Nesting

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        max_length = 0
        
        for i in range(len(nums)):
            if not visited[i]:
                temp_length = 0
                k = nums[i]
                
                while True:
                    k = nums[k]
                    temp_length = temp_length + 1
                    visited[k] = True
                    
                    if k == nums[i]:
                        break
            max_length = max(temp_length, max_length)
        
        return max_length