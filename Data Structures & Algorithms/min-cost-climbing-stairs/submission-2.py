class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) <= 2:
            return min(cost[0], cost[1])
        dp = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            print(cost[i], dp[0], dp[1])
            temp = dp[1]
            dp[1] = cost[i] + min(temp, dp[0])
            dp[0] = temp

        print(dp[0], dp[1])
        return min(dp[0], dp[1])