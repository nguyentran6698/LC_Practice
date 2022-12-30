from ast import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        slots = sorted(intervals ,key=lambda x: x[0])
        free_rooms = []
        heapq.heappush(free_rooms,slots[0][1])
        for time in slots[1:]:
            
            if free_rooms[0] <= time[0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms,time[1])
        return len(free_rooms)

# 2 pointers approach
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        used_rooms = 0
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)
        end_pointer = 0
        start_pointer = 0
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms