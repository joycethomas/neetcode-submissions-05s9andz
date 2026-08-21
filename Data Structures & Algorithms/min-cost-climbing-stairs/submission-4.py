class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1 = cost[-1]
        step2 = cost[-2]
        count = len(cost) - 3

        while count >= 0:
            temp = cost[count] + min(step1, step2)
            step1, step2 = step2, temp
            count -= 1
        
        return min(step1, step2)