class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        
        for x in range(1, len(intervals)):
            #this one's only wrong bc neet put it in tuples
            #if intervals[x][0] >= intervals[x - 1][0] and intervals[x][0] < intervals[x-1][1]:
            if intervals[x].start >= intervals[x - 1].start and intervals[x].start < intervals[x-1].end:
                return False
        return True