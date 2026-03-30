class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                result = max(prices[j] - prices[i], result)
            
        return result
        