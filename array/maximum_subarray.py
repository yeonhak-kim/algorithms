# Maximum Subarray

# find the maximum sum from among every possible subarray in array nums.

def maxSubArray(self, nums: List[int]) -> int:
    local_sum = max_sum = nums[0]
    
    for num in nums[1:]:
        local_sum = max(num, local_sum + num)
        max_sum = max(max_sum, local_sum)
    
    return max_sum