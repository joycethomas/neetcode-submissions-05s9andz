class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0
        r = 1
        result = 0
        while r < len(prices):
            print(prices[l], prices[r])
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                result = max(result, prices[r] - prices[l])
                r += 1
            
        return result

        '''result = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                result = max(prices[j] - prices[i], result)
            
        return result'''
        