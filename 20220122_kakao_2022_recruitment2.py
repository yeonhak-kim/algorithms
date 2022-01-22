# Kakao Open Recruitment Question 1

import math
def solution(n, k):
    # check for prime-ness
    def is_prime(num:float) -> bool:
        if num <= 1: return False
        
        factor = 2
        # iterating upto sqrt(num + 1) is enough
        while factor < math.sqrt(num + 1):
            if num % factor == 0:
                return False
            factor += 1
        
        return True
    
    # converts n(decimal) to k-base number
    def base_converter(num:int, k:int) -> str:
        if num < 1: return ''
        
        rems = []
        while num:
            num, rem = divmod(num, k)
            rems.append(str(rem))
        
        return ''.join(reversed(rems))
    
    # converted number in string
    k_base = base_converter(n, k)
    
    # parse data
    candidates = k_base.split('0')
    
    # initialzie counter
    counter = 0
    # count the number of prime
    for candidate in candidates:
        if candidate == '': continue
        if is_prime(float(candidate)):
            counter += 1
            
    return counter