class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #need a dp array to keep track after every iteration of coins being added
        #also need a way to keep track of the amount of coins
        dp = {}
        def change(i, total):
            if total == 0:
                return 0
            if (i, total) in dp:
                return dp[(i, total)]
            if i < 0 or total < 0:
                return float('inf')
            if coins[i] <= total: 
                dp[(i, total)] = min(1 + change(i, total - coins[i]), change(i - 1, total)) 
                return dp[(i, total)]
     
    
            return change(i - 1, total)
        

        result = change(len(coins) - 1, amount)
        if result == float('inf'):
            return -1
        return result


            
        