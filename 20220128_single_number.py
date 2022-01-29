# Single Number


# Cache (O(N)) vs Sort (O(NlogN))
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def memorization_ver() -> int:
            seen = set()
            
            for num in nums:
                if num not in seen: 
                    seen.add(num)
                    continue
                
                if num in seen:
                    seen.remove(num)
            
            return seen.pop()
        
        def sorting_ver() -> int:
            if len(nums) == 1: return nums[0]
            
            sorted_nums = sorted(nums)
            
            l, r = 0, 1
            while r < len(sorted_nums):
                if sorted_nums[l] != sorted_nums[r]:
                    return sorted_nums[l]
                l += 2
                r += 2
                
            return sorted_nums[-1]
        
        return memorization_ver()
                
                