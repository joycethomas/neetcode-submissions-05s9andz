class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0

        first = 0
        second = len(height) - 1
        firstmax = height[first]
        secondmax = height[second]
        result = 0

        while first < second: 
            if firstmax < secondmax:
                first += 1
                firstmax = max(firstmax, height[first])
                result += firstmax - height[first]
            else:
                second -= 1
                secondmax = max(secondmax, height[second])
                result += secondmax-height[second]
                

    

        return result
        