class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1, y1, x2, y2):
            return math.sqrt((x1 - x2)**2 +(y1 - y2)**2)
        
        dist = []
        for p in points:
            pdis = -1 * distance(p[0], p[1], 0, 0)
            heapq.heappush(dist, (pdis, p))
            if len(dist) > k:
                heapq.heappop(dist)
        
        results = []
        for x in dist:
            results.append(x[1])

        return results