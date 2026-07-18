class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for x in tasks:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        #make a max heap, pop n so that you can have one of each, and then push it back
        #if the max heap is empty but there's still n left, then we add idle

        heap = []
        for x, y in dic.items():
            heap.append(-1 * y)
        heapq.heapify(heap)
        
        q = deque()

        result = 0
        time = 0
        while heap or q:
            time += 1
            if heap:
                curr = 1 + heapq.heappop(heap)
                if curr:
                    q.append((curr, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
            
        
        return time


        
        


        