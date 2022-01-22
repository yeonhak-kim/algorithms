# Two Sum (leetcode)

# Hash Map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Take advantage of the fact below and hash
        # x + y = target
        # y = target - x
        
        # Initialize cache
        mapping = {}
        
        # Main logic: hash key(target - num) : value(index) 
        for i, num in enumerate(nums):
            if num in mapping:
                # Found two sum indices
                return[i, mapping[num]]
            
            mapping[target - num] = i
        
        # Code will not reach here since the solution always exists(given condition)
        return [None]