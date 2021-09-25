# Merge Sorted Array
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    left, right = nums1[:m], nums2
    L = R = i = 0
    
    while L < m and R < len(nums2):
        if left[L] <= right[R] :
            nums1[i] = left[L]
            L += 1
        else:
            nums1[i] = right[R]
            R += 1
        
        i += 1
    
    while L < m:
        nums1[i] = left[L]
        i += 1
        L += 1
    
    while R < len(nums2):
        nums1[i] = right[R]
        i += 1
        R += 1