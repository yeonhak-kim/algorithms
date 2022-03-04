# Meeting Room (leetcode)

# priority queue
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort intervals
        intervals.sort(key=lambda x:x[0])
        # initialize heap
        free_rooms = [intervals[0][1]]
        heapq.heapify(free_rooms)
        # main logic
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # deoccupy a meeting room
            if free_rooms[0] <= start:
                heapq.heappop(free_rooms)
            # occupy meeting room
            heapq.heappush(free_rooms, end)
        
        return len(free_rooms)
                    
        
        
        