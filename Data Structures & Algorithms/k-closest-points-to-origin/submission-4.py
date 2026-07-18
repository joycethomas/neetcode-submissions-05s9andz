class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        x1, y1 = 0, 0

        for x2, y2 in points:
            #dis = -1 * (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
            dis = (x2**2 + y2**2) * -1
            heapq.heappush(minHeap, (dis, (x2, y2)))
            #print(minHeap)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        print(minHeap)
        res = []
        for x, y in minHeap:
            res.append(y)
        return res