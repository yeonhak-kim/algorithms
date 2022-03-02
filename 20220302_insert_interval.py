# Insert Interval (leetcode)

# Greedy Algorithm
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        new_start, new_end = newInterval
        idx, N = 0, len(intervals)
        result = []
        
        while idx < N and new_start > intervals[idx][0]:
            result.append(intervals[idx])
            idx += 1
        
        # handle new_start of the interval; merge or not merge
        if not result or new_start > result[-1][1]:
            result.append(newInterval)
        else:
            result[-1][1] = max(new_end, result[-1][1])
        
        # handle end range
        
        while idx < N:
            start, end = intervals[idx]
            if result[-1][1] < start:
                result.append(intervals[idx])
            else:
                result[-1][1] = max(result[-1][1], end)
            idx += 1
            
        return result