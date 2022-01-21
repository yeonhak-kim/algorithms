# Longest Common Sequence (leetcode)

# Top Down Approach (Recursive + Memoization)
class SolutionOne:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def LCS(idx1:int, idx2:int) -> int:
            # Termination case
            if idx1 == len(text1) or idx2 == len(text2): return 0
            # Cached result
            if (idx1, idx2) in memo: return memo[(idx1, idx2)]
            
            # Case1: text1[idx1] not counted as the longest common sequence
            case1 = LCS(idx1 + 1, idx2) 
            case2 = 0
            
            first_occurrence = text2.find(text1[idx1], idx2)
            if first_occurrence >= 0:
                # Case2: if text1[idx1] has been found in text2
                case2 = 1 + LCS(idx1 + 1, first_occurrence + 1)
            
            memo[(idx1, idx2)] = max(case1, case2)
            return max(case1, case2)

        # Initialize cache
        memo = {}
        return LCS(0, 0)

# Top Down Approach (Recursive + Memoization) + Slight Optimization
class SolutionTwo:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def LCS(idx1:int, idx2:int) -> int:
            # Termination case
            if idx1 == len(text1) or idx2 == len(text2): return 0
            # Cached result
            if (idx1, idx2) in memo: return memo[(idx1, idx2)]
            
            if text1[idx1] == text2[idx2]:
                # Case1: current positions explicit same char
                memo[(idx1, idx2)] = 1 + LCS(idx1 + 1, idx2 + 1)
                return memo[(idx1, idx2)]
            else:
                # Case2: current positions do not result in same char
                memo[(idx1, idx2)] = max(LCS(idx1, idx2 + 1), LCS(idx1 + 1, idx2))
                return memo[(idx1, idx2)]
            
        # Initialize cache
        memo = {}
        return LCS(0, 0)

# Bottom Up Approach (Iteration)
class SolutionThree:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize 2D dp array
        dp_grid = [[0]*(len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Main Logic: iterate from backwards and solve subproblem
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    # Case1: when same char encountered
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                
                else:
                    # Case2: when different char
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
        return dp_grid[0][0]