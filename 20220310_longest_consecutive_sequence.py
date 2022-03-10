# Longest Consecutive Sequence

# Intelligent Hash Map
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_map = set(nums)
        
        longest_sequence = 0
        for num in number_map:
            if num - 1 not in number_map:
                current_sequence = 1
            
                while num + 1 in number_map:
                    current_sequence += 1
                    num += 1

                longest_sequence = max(longest_sequence, current_sequence)
            
        return longest_sequence
        