# Two Sum 2 - Input array is sorted
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
    # Solution 1: two pointers
    l, r = 0 , len(numbers) - 1
    while l < r:
        current_sum = numbers[l] + numbers[r]
        if current_sum == target:
            return [l + 1, r + 1]
        
        if current_sum < target:
            l += 1
        
        if current_sum > target:
            r -= 1
    
    '''
    # Solution 2: binary search (worst: O(nlog(n)), average: O(log(n)))
    
    l, r = 0, len(numbers) - 1
    while l < r:
        mid = (l + r) // 2
        current_sum = numbers[l] + numbers[r]
        right_sum = numbers[mid] + numbers[r]
        left_sum = numbers[l] + numbers[mid]
        
        if(current_sum == target):
            return [l + 1, r + 1]
        if(current_sum < target):
            l = mid if numbers[mid] + numbers[r] < target else l + 1
        if(current_sum > target):
            r = mid if numbers[mid] + numbers[l] > target else r - 1
    '''