class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x:x[0])
        result = []
        result.append(intervals[0])
        curr = result[0]


        for x in range(1, len(intervals)):
            print(curr, intervals[x])
            if intervals[x][0] <= curr[1]: #and intervals[x][0] <= curr[1]: THIS WAS LITERALLY THE FUCKING FIX I NEEDED AND IT WOULD'VE FUCKING WORKED FUCK YOU
                curr[1] = max(intervals[x][1], curr[1])
            else:
                result.append(intervals[x])
                curr = result[-1]

        return result