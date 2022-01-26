# Maximum Subarray (leetcode)

# Global and Local Maxima
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # it is guranteed that the input nums is not empty
        
        # initialize local and global maxima
        global_maxima = local_maxima = -10**4
        
        # iterate through array and collect local and global maxima
        for num in nums:
            local_maxima = max(local_maxima + num, num)
            global_maxima = max(global_maxima, local_maxima)
        
        return global_maxima