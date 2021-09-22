# Move Zeroes
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0:
        return nums
    
    start = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1