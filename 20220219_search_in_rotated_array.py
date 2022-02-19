# Search in Rotated Array (leetcode)

# One Pass Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target: return mid
            
            if nums[mid] >= nums[start]:
                # mid is part of the left increasing sequence
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # mid is part of the right increasing sequence
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1