# Sort Colors (leetcode)

# Dutch National Flag Problem
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort intervals
        intervals.sort(key=lambda x:x[0])
        # heap
        free_rooms = [intervals[0][1]]
        heapq.heapify(free_rooms)
        # counter
        last_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if free_rooms[0] <= start:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, end)
        
        return len(free_rooms)
                    
        
        
        