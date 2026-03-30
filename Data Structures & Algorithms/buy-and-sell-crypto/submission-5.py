class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #L R
        if len(prices) == 1:
            return 0
        profit = 0
        l, r = 0, 1
        while r <= len(prices) - 1: #for l in range(0, len(prices) - 1):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r = l + 1
        return profit


        