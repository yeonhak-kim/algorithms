# First Bad Version
# isBadVersion is given API from the system. The goal is to call an API as less possible

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left,right = 1, n
    
    slave_index = 1
    while left <= right:
        # little optimization 
        if isBadVersion(slave_index) is True:
            return slave_index
        
        # regular binary search
        index = left + (right - left) // 2
        
        # search left
        if isBadVersion(index) is True:
            right = index - 1
        # search right
        else:
            left = index + 1
    
    # assuming that there is a faulty product, after the binary search, index will be the last element been look upto
    # thus, it would either case where index be the faulty product or the previous be the faulty product which is index + 1
    return index + 1 if not isBadVersion(index) else index