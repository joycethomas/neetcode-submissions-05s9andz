class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for x in range(len(stones)):
            stones[x] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            '''if x > y: #x weighs less
                y = y + (x * -1)
                #print(y)
                heapq.heappush(stones, y - x)''' 
            #^^ DON'T NEED THIS PART BECAUSE IT'S ALREADY IN ORDER
            if x < y:
                #x = x + (y * -1)
                #print(x)
                heapq.heappush(stones, x - y)
        
        if len(stones) == 1:
            return stones[0] * -1
        return 0