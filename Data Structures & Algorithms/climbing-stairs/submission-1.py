class Solution:
    def climbStairs(self, n: int) -> int:
        step1 = 1
        step2 = 1
        count = 0

        while count < n:
            step1, step2 = step2, step1 + step2

            count += 1
        
        return step1