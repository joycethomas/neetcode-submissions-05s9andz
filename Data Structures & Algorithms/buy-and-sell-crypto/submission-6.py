class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        record = 0

        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            print(record, prices[buy], prices[sell], prices[sell] - prices[buy])
            if prices[sell] - prices[buy] > record:
                record = prices[sell] - prices[buy]
        
        if record <= 0:
            return 0
        return record

        