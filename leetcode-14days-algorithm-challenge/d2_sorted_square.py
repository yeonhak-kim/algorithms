# Squares of a Sorted Array
def sortedSquares(self, nums: List[int]) -> List[int]:
    result = [0] * len(nums)
    L, R = 0, len(nums) - 1
    index = len(nums) - 1
    
    while L <= R:
        if abs(nums[L]) > abs(nums[R]):
            result[index] = pow(nums[L], 2)
            L += 1
        else:
            result[index] = pow(nums[R], 2)
            R -= 1
        index -= 1
    return result