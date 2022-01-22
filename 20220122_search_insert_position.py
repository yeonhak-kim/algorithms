# Search Insert Position (leetcode)

# Binary Search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # initialize left and right pointers
        L, R = 0, len(nums) - 1
        
        # binary search
        while L <= R:
            # floor
            mid = int((L + R)/2)
            if nums[mid] == target: return mid
            
            if nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        
        return L