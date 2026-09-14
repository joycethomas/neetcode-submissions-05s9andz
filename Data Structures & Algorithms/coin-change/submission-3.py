class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N, M = len(coins), amount 
        dp = [float('inf')] * (M + 1)
        dp[0] = 0

        #thinking of it in terms of like max profit, but need to think of it in terms of amount of coins
        #what should the dp be keeping track of?
        for i in range(N):
            curr = [float('inf')] * (M + 1)
            for c in range(M + 1):
                skip = dp[c]
                include = float('inf')
                if c - coins[i] >= 0:
                    include = 1 + curr[c - coins[i]]
                curr[c] = min(skip, include)
            dp = curr
        if dp[-1] == float('inf'):
            return -1      
        return dp[-1]