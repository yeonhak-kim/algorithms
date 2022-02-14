# Container with Most Water (leetcode)


# Two Pointers
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_volume = 0
        while l < r:
            local_volume = min(heights[l], heights[r])*(r - l)
            max_volume = max(local_volume, max_volume)
            
            # always keep the highest height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_volume
            