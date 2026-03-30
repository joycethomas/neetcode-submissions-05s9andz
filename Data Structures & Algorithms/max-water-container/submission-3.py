class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                temp = abs(min(heights[l], heights[r]) * (l - r))
                print(heights[l], heights[r], temp)
                if temp > result:
                    result = temp

        


        return result
            