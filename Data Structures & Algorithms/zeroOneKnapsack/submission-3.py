class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [[0] * (M + 1) for n in range(N)]

        for i in range(M + 1):
            if i >= weight[0]:
                dp[0][i] = profit[0]


        for i in range(N):
            for j in range(M + 1):
                skip = dp[i - 1][j]
                include = 0
                if j >= weight[i]:
                    include = profit[i] + dp[i - 1][j - weight[i]]
                dp[i][j] = max(skip, include)



        return dp[N-1][M]