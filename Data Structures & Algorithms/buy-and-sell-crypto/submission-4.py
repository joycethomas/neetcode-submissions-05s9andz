class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #L R
        if len(prices) == 1:
            return 0
        profit = 0
        for l in range(0, len(prices) - 1):
            r = l + 1
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            while (r <= len(prices) - 1) and (prices[l] <= prices[r]):
                if prices[l] > prices[r]:
                    l = r
                    r += 1
                    break
                curr = prices[r] - prices[l]
                profit = max(profit, curr)
                r += 1


        return profit


        