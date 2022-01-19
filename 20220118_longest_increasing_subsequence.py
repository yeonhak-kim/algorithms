# Longest Increasing Subsequence (leetcode)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # initialize dp array of size |nums|
        max_lengths = [1]*len(nums)
        # initialize result
        max_length = 0
        for i in range(len(nums)):
            max_lengths[i] = 1 + max(
                (max_lengths[j] for j in range(i) if nums[i] > nums[j]), default=0)
            max_length = max(max_length, max_lengths[i])
            
        return max_length
            