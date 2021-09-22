# Binary Search
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        index = left + (right - left) // 2
        # match
        if nums[index] == target:
            return index
        # search right
        if nums[index] < target:
            left = index + 1
        # search left
        else:
            right = index - 1
        
    return -1