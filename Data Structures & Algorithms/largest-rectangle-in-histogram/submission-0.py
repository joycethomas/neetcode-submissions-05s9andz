class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = []

        for i, h in enumerate(heights):
            start = i #if it doesn't go through the loop, it'll add it's own start index
            while stack and stack[-1][1] > h: #keeps popping all the ones that are higher than the one we're on
                index, height = stack.pop()
                maxA = max(maxA, height * (i - index))
                start = index #like backtracking
            stack.append((start, h))

        for i, h in stack: #for the numbers left in the stack that extend all the way to the end
            maxA = max(maxA, h * (len(heights) - i)) #these ones only stay if they can stretch all the way to the end
        return maxA





        '''for i, h in enumerate(heights):
            while stack and stack[-1][1] > h: #if the top of the stack is more than current height
                val = stack.pop
                stack.append((i, val[1], h))
                if val[1] == val[2]:
                    pot = 1
                else:
                    pot = (val[1] - val[0]) 
                pot *= val[2]
                maxheight = max(maxheight, pot)
            stack.append((i, i, h))'''