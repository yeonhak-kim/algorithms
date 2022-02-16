# Letter Combination of Phone Number

# Backtracking (DFS/Recursion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # pre-process digit-to-letter mapping
        digit_decoder = {'1': None,
                        '2': 'abc',
                        '3': 'def',
                        '4': 'ghi',
                        '5': 'jkl',
                        '6': 'mno',
                        '7': 'pqrs',
                        '8': 'tuv',
                        '9': 'wxyz',
                        '0': None}
        
        def mapping(prefix:str, digit_pointer:int) -> str:
            if digit_pointer == len(digits):
                return prefix
            
            letters = digit_decoder[digits[digit_pointer]]
            
            for letter in letters:
                letter_combined = mapping(prefix + letter, digit_pointer + 1)
                if letter_combined:
                    result.append(letter_combined)
		        
						# at every end of loop (finishing each digit), will return ''
            return ''
        
        
        result = []
        
        mapping('', 0)
        return result