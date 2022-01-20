# Valid Parentheses (leetcode)
class Solution:
    def isValid(self, s: str) -> bool:
        
        # initialize stack that tracks the brackets
        stack = []
        # mapping for brackets pair
        mapping = {')':'(', '}':'{', ']':'['}
        
        # main logic: pop when closed bracket has been encountered
        for char in s:
            if char in mapping and stack:
                prev_char = stack.pop()
                
                # bracket mis-match: invalid
                if mapping[char] != prev_char:
                    return False
                
            else:
                stack.append(char)
            
        # no remaining brackets for valid parentheses
        return True if not stack else False