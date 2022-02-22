# Find first and last element in a sorted array

# Two Binary Search Passes
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # first implement regular binary search 
        # then expand from the found element to left right and find the boundary
        
        if not nums:
            return [-1, -1]
        
        
        def findbound(is_left_bound: bool) -> int:
            nonlocal target
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] == target:
                    
                    if is_left_bound:
                        if mid == l or nums[mid - 1] < target:
                            return mid
                        
                        r = mid - 1
                    
                    if not is_left_bound:
                        if mid == r or nums[mid + 1] > target:
                            return mid
                        
                        l = mid + 1          

                if nums[mid] > target:
                    # target is in the left half
                    r = mid - 1
                if nums[mid] < target:
                    # target is in the right half
                    l = mid + 1
            
            return -1
        
        left_bound = findbound(is_left_bound=True)
        
        if left_bound == -1:
            return [-1, -1]
        
        right_bound = findbound(is_left_bound=False)
        
        return [left_bound, right_bound]
        