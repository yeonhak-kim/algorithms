# Permutation in String
# Sliding Window

def checkInclusion(self, s1: str, s2: str) -> bool:
    
    '''
    # Very Slow #
    # Solution using dictionary, sliding window
    lib = dict.fromkeys(s1, 0)
    for c1 in s1:
        lib[c1] += 1
    
    # s1 length
    n = len(s1)
    
    # s2 length
    m = len(s2)
    
    L, R = 0, n - 1
    
    local_lib = dict.fromkeys(s1, 0)
    while L <= R and R < m:
        c2 = s2[L]
        if c2 in local_lib:
            local_lib[c2] += 1
            # drop key
            if local_lib[c2] == lib[c2]:
                del local_lib[c2]
                
        # reset the window
        else:
            local_lib = dict.fromkeys(s1, 0)
            if c2 in lib:
                L = R - n + 1
                R += 1
            else:
                R = L + n
        L += 1
    
    return False if local_lib else True
    '''
    # Solution using fixed array, sliding window
    
    # take advantage on that there are only 26 chars in alphabet
    # target array index -> 0 : a, 1 : b, ...., 25: z
    target = [0] * 26
    for c1 in s1:
        idx1 = ord(c1) - ord('a')
        target[idx1] += 1
        
    window = [0] * 26
    for i, c2 in enumerate(s2):
        idx2 = ord(c2) - ord('a')
        window[idx2] += 1
        
        # we are sliding window by the length of s1
        if i >= len(s1):
            to_drop = ord(s2[i - len(s1)]) - ord('a')
            window[to_drop] -= 1
        # check if window == target
        if window == target:
            return True
    
    return False