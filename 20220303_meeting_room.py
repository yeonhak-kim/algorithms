# Meeting Room (leetcode)

# Sorting and Greedy Appoach
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        # sort intervals by meeting start time
        intervals.sort(key=lambda x:x[0])
        # initialized starting point
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # condition check
            if last_end > start:
                return False
            last_end = end
        
        return True