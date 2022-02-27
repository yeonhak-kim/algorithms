# Permutations (leetcode)

# Backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        N = len(nums)
        result = []
        def backtrack(permutation, seen) -> None:
			# non-local variables
            nonlocal N 
            nonlocal nums
            nonlocal result
            
			# base case (termination)
            if len(permutation) == N:
                result.append(permutation[:])
                return
            
            for num in nums:
                # check for duplicates
                if num in seen:
                    continue
                    
                # add new combination
                permutation.append(num)
                seen.add(num)
                
                # backtrack call
                backtrack(permutation, seen)
                
                # clean up
                permutation.pop()
                seen.discard(num)
            
            return
        
        backtrack([], set())
        return result
