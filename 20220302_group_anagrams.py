# Group Anagrams (leetcode)

# Cache via letter occurence
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize cache
        cache = {}
        # initialize result
        result = []
        # main logic
        for word in strs:
            # letter occurence ; representation of the word via letter occurence
            letter_occurence = [0]*26
            # build letter occurence
            for letter in word:
                letter_occurence[ord(letter) - ord('a')] += 1
            letter_occurence = tuple(letter_occurence)
            
            # key and result insertion
            if letter_occurence not in cache:
                cache[letter_occurence] = len(cache)
                result.append([word])
            else:
                result[cache[letter_occurence]].append(word)
        
        return result
            
            
            