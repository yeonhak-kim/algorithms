# Word Break (leetcode)

# Recursion + memo
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def search(idx):
            nonlocal s
            nonlocal n
            nonlocal word_dict
            
            if idx == n:
                return True
            
            subword = []
            for i in range(idx, n):
                subword.append(s[i])
                if ''.join(subword) in word_dict and i + 1 not in cache and search(i + 1):
                    return True
                
            cache.add(idx) 
            return False
        
        # create hash map for the wordDict
        word_dict = set(wordDict)
        cache = set()
        n = len(s)
        
        return search(0)
        
                    