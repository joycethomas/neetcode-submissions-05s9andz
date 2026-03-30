class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0

        L, R = 0, len(heights)-1
        while L < R:
            minh = min(heights[L], heights[R])
            total = minh * (R-L)
            if total > max:
                max = total 
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return max

