# Two Sum
def twoSum(self, nums, target):
    lib = {}
    for i in range(len(nums)):
        if (target - nums[i]) in lib:
            return [i, lib[target - nums[i]]]
        else:
            lib[nums[i]] = i