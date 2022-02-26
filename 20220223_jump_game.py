# Jump Game (leetcode)

# Modified Top-Down
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        track = N - 1
        
        for idx in range(N - 2, -1, -1):
            if idx + nums[idx] >= track:
                track = idx
            
        return track == 0
            

# Top-Down (iterative version)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*(len(nums))
        dp[-1] = True
        for idx in range(len(nums) - 2, -1, -1):
            max_jump = min(idx + nums[idx], len(nums) - 1)
            for i in range(idx + 1, max_jump + 1):
                if dp[i]:
                    dp[idx] = True
                    break
        return dp[0]
        

# Bottom-Up (recursive version)
# class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = set()
        END_INDEX = len(nums) - 1
        def jump(curr_idx:int):
            nonlocal END_INDEX
						# base case
            if curr_idx >= END_INDEX:
                return True
            
						# cache
            if curr_idx in cache:
                return False
            
						# minor optimization
            end = min(END_INDEX - curr_idx, nums[curr_idx])
						# recursive call
            for jump_step in range(end, 0, -1):
                if jump(curr_idx + jump_step):
                    return True
            
            cache.add(curr_idx)
            
            return False
        
        return jump(0)    