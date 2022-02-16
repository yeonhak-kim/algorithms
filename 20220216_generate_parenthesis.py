# Generate Parenthesis


# Backtracking

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(prefix:str, num_open: int, num_close:int) -> List[str]:
            nonlocal n
            nonlocal result
            
            if num_open == num_close == n:
                result.append(prefix)
                return prefix
            
            # precede opening bracket first
            if num_open < n:
                parenthesis = generate(prefix + '(', num_open + 1, num_close)
            
            # precede closing bracket only when number of open
            if num_close < num_open:
                parenthesis = generate(prefix + ')', num_open, num_close + 1)
             
        result = []
        generate('', 0, 0)
        return result