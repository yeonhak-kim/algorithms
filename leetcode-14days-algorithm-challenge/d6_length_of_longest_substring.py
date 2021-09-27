# Longest Substring Without Repeating Characters
# Sliding Window
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0 or len(s) == 1:
        return 0 if len(s) == 0 else 1
    
    last_occurrence = {}
    L = R = 0
    max_length = 1
    
    while R < len(s):
        if s[R] not in last_occurrence:
            last_occurrence[s[R]] = R
            
        else:
            if L <= last_occurrence[s[R]]:
                L = last_occurrence[s[R]] + 1
            last_occurrence[s[R]] = R
        
        local_length = R - L + 1
        max_length = max(max_length, local_length)
        R += 1
            
    return max_length