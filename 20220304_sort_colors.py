# Sort Colors (leetcode)

# Dutch National Flag Problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_end, curr, blue_start = 0, 0, len(nums) - 1
        
        while curr <= blue_start:
            if nums[curr] == 0:
                # red
                nums[red_end], nums[curr] = nums[curr], nums[red_end]
                red_end += 1
                curr += 1
            
            elif nums[curr] == 2:
                # blue
                nums[blue_start], nums[curr] = nums[curr], nums[blue_start]
                blue_start -= 1
            else:
                curr += 1
        
        
                