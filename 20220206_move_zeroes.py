# Move Zeroes (leetcode)

# move zeroes to right
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_start = 0
        while zero_start < len(nums):
            if nums[zero_start] == 0:
                break
            
            zero_start += 1
        
        if zero_start == len(nums) - 1: return
        
        zero_length = 1
        while zero_start + zero_length < len(nums):
            if nums[zero_start + zero_length] == 0: 
                zero_length += 1
                continue
            
            nums[zero_start], nums[zero_start + zero_length] = nums[zero_start + zero_length], nums[zero_start]
            zero_start += 1
        
        return


# move non-zeroes to left
class Solution:
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