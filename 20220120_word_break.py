# Word Break (leetcode)

# Top Down Approach (Recursive)
class SolutionOne:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Hashable set for O(1) access
        word_set = set(wordDict)
        # Initialize cache
        memo = {}
        
        def subwordBreak(s:str, start:int) -> bool:
            # Base case
            if start == len(s): return True
            # Cache
            if start in memo: return memo[start]
            
            # Main Logic: s[0:start] represents subproblem
            for end in range(start + 1, len(s) + 1):
                if (s[start:end] in word_set) and subwordBreak(s, end):
                    # Subproblem s[0:start] can be broken down by the wordDict
                    memo[start] = True
                    return True
                
            # Subproblem s[0:start] fail to break down into words
            memo[start] = False
            return False
        
        return subwordBreak(s, 0)

# Bottom Up Approach (Iteration)
class SolutionTwo:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
				# Hashable set for O(1) access
        word_set = set(wordDict)
				# Initiaize dp array of size len(s) + 1
        dp = [True] + [False]*len(s)
				
				# Main Logic: solve every subproblem which each requires examination of
				# all possible generation of prefixes.
        for end in range(1, len(s) + 1):
            for start in range(end):
								# Utilize dp
                if dp[start] and s[start:end] in word_set:
                    dp[start] = True
                    break

        return dp[len(s)]