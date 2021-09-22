# Search Insert Position
def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    slave_index = 0
    
    while left <= right:
        # little optimizaiton: only useful if target exists in nums on front position
        if nums[slave_index] < target:
            if nums[slave_index] == target:
                return slave_index
        
        # regular binary search
        index = left + (right - left) // 2
        
        # match 
        if nums[index] == target:
            return index
        # search left
        if nums[index] > target:
            right = index - 1
        # search right 
        else:
            left = index + 1
        
    
    return index if nums[index] > target else index + 1