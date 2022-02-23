# Combination Sum (leetcode)


# Backtracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def find(arr:List[int], first_candidate:int, target:int):
            nonlocal result
            # base case
            if target == 0:
                result.append(arr[:])
                return
            
            # recursive call
            for idx in range(first_candidate, len(candidates)):
                candidate = candidates[idx]
                if candidate <= target:
                    arr.append(candidate)
                    find(arr, idx, target - candidate)
                    arr.pop()
                
            return
        
        find([], 0, target)
        return result
            