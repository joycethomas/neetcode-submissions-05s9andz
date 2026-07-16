class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #turn the vals neg to make it a max heap
        for i in range(len(stones)):
            stones[i] *= -1
       
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            s1 = abs(heapq.heappop(stones))
            s2 = abs(heapq.heappop(stones))
            print(s1, s2)
            if s1 == s2:
                continue
            if s1 < s2:
                s2 -= s1
                heapq.heappush(stones, s2 * -1)
            else:
                s1 -= s2
                heapq.heappush(stones, s1 * -1)

        if stones:
            return abs(stones[0])
        return 0