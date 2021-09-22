# Rotate Array

def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    '''
    # Solution 1: using extra space
    result = [0] * len(nums)
    for i in range(len(nums)):
        result[(i + k) % (len(nums))] = nums[i]
    
    # this is required because we want to modify the nums array.("nums = result" will not work since it will allocate new array(new address to the variable nums))
    for i in range(len(nums)):
        nums[i] = result[i]
    '''
    
    # Solution 2: cyclic replacement, two pointers
    n = len(nums)
    k %= n
    
    start = count = 0
    while count < n:
        i, current = start, nums[start]
        while True:
            j = (i + k) % n
            nums[j], current = current, nums[j]
            i = j
            count += 1
            if i == start:
                break
        start += 1