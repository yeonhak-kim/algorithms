# Intersection of Two Arrays 2
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    lib1, lib2 = self.createDict(nums1), self.createDict(nums2)
    n, m = len(nums1), len(nums2)
    if n <= m:
        return self.intersection(lib1, lib2)
    else:
        return self.intersection(lib2, lib1)
    
    
    
def createDict(self, nums: List[int]) -> dict:
    lib = {}
    for i in range(len(nums)):
        if nums[i] not in lib:
            lib[nums[i]] = 1
        else:
            lib[nums[i]] += 1
    return lib

def intersection(self, smaller: dict, larger: dict) -> List[int]:
    # put smaller sized dictionary as a first argument for optimization.
    intersection = []
    for key in smaller:
        if key not in larger:
            continue
        
        # intersection found
        if smaller[key] <= larger[key]:
            intersection = intersection + [key] * smaller[key]
        else:
            intersection = intersection + [key] * larger[key]
    
    return intersection