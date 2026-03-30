class Solution:
    #  TRY AGAIN WITH TWO POINTER, 
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        j = len(heights) - 1
        i = 0
        while i < j:
            print(heights[i], heights[j])
            temp = min(heights[i], heights[j]) * abs(i - j)
            result = max(temp, result)
            if heights[i] < heights[j]: 
                i += 1
            else:
                j -= 1
        
        return result

        
        
        '''result = 0
        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                temp = abs(min(heights[l], heights[r]) * (l - r))
                print(heights[l], heights[r], temp)
                if temp > result:
                    result = temp
        return result'''
            