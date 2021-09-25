# Contains Duplicate
def containsDuplicate(self, nums: List[int]) -> bool:
    
    """
    #Using set to check duplicate
    _set = set();
    length = len(nums)
    for i in range(length):
        _set.add(nums[i])
    
    return True if length != len(_set) else False
    """
    
    return True if len(set(nums)) < len(nums) else False