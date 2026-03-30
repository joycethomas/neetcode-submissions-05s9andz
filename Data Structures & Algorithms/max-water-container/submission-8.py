class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights) - 1
        maxh = min(heights[first], heights[last]) * (last - first) 
        while first < last: 
            maxh = max(min(heights[first], heights[last]) * (last - first), maxh)
            if heights[first] <= heights[last]:
                first += 1
            else:
                last -= 1
        return maxh


