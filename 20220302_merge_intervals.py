# Merge Intervals (leetcode)

# Greedy Algorithm
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the array 
        intervals.sort(key=lambda x:x[0])
        # logic for merging intervals
        idx, N = 1, len(intervals)
        result = [intervals[0]]
        while idx < N:
            start, end = intervals[idx]
            if result[-1][1] < start:
                # append
                result.append(intervals[idx])
            else:
                # merge
                result[-1][1] = max(result[-1][1], intervals[idx][1])
            idx += 1
        return result
            
        