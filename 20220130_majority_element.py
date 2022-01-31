# Majority Element

# O(1) solution by sorting the array
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort nums in order to save memory (avoid using cache)
        nums_copy = sorted(nums)
        
        # instantiate value and count variables
        val, count = float('inf'), 0
        for num in nums_copy:
            # found majority element
            if count > len(nums) / 2: break
            
            if num != val:
                # update value and counter
                val = num
                count = 1
            else:
                # count current element
                count += 1
        
        return val

# cache
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache = {}
        
        for num in nums:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1
                
            if cache[num] > len(nums) / 2: return num
        
        return None