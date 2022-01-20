# Combination Sum (leetcode)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        
        def backtrack(remaining:int, combination:List[int], remaining_candidates):
            if remaining == 0:
                # deepcopy combination and append it to the result
                result.append(list(combination))
                return
            if remaining < 0:
                return
            
            # main logic 
            for idx, candidate in enumerate(remaining_candidates):
                combination.append(candidate)
                # pass the remaining candidates to the backtrack call (combination)
                backtrack(remaining - candidate, combination, remaining_candidates[idx:])
                combination.pop()
            
        backtrack(target, [], candidates)
        return result