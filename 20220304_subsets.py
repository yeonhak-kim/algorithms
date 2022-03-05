# Subsets (leetcode)

# backtrack
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start:int, subset:List[int]):
            nonlocal result
            nonlocal k
            nonlocal N
            if len(subset) == k:
                result.append(subset[:])
                return
            
            for i in range(start, N):
                # build subset
                subset.append(nums[i])
                # recursive call
                backtrack(i + 1, subset)
                # backtrack
                subset.pop()
            
            return
        
        # initialize variables
        result = []
        N = len(nums)
        
        # find subsets by size k
        for k in range(N + 1):
            backtrack(0, [])
        
        return result
            
            