"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #intervals.sort(key=lambda x: x[0])
        #another idea is just to merge all the intervals that are to get

        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])
        '''start = []
        end = []
        for x in range(len(intervals)):
            start.append(intervals[x].start)
            end.append(intervals[x].end)'''
        print(start, end)
        
        s = 0
        e = 0

        count = 0
        rooms = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            rooms = max(rooms, count)
        
        return rooms