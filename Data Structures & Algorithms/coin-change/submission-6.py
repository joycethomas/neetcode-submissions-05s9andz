class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N, M = len(coins), amount
        dp = [float('inf')] * (M + 1)
        dp[0] = 0

        for i in range(N):
            for c in range(M + 1):
                #print(i, c)
                skip = dp[c]
                include = float('inf')
                if c - coins[i] >= 0:
                    include = 1 + dp[c - coins[i]]
                #print(skip, include)
                dp[c] = min(skip, include)
            print(dp)

        if dp[-1] == float("inf"):
            return -1
        return dp[-1]