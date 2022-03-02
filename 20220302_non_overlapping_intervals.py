# Non-Overlapping Intervals (leetcode)

# Sorting + Greedy Approach
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        idx, N = 1, len(intervals)
        last_end = intervals[0][1]
        count = 0
        while idx < N:
            start, end = intervals[idx]
            
            if last_end <= start:
                # no overlap 
                last_end = end
            else:
                # this incorporates two cases
                # case 1: last_end ending before end -> must remove current range
                # case 2: last_end ending after end -> must remove previous range
                last_end = min(last_end, end)
                count += 1
                
            idx += 1
        
        return count
                