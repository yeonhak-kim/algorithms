# Two Sum

# given target value, find two indices i, j where num[i] + num[j] = target
# it is assumed that there will always be an answer
def twoSum(self, nums, target):
        lib = {}
        for i in range(len(nums)):
            if (target - nums[i]) in lib:
                return [i, lib[target - nums[i]]]
            else:
                lib[nums[i]] = i