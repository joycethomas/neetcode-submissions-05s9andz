class MedianFinder:

    def __init__(self):
        self.right = []
        self.left = []
        heapq.heapify(self.right)
        heapq.heapify(self.left)
        

    def addNum(self, num: int) -> None:
        num = float(num)
        if not self.left:
            heapq.heappush(self.left, num)
        elif self.left and num > self.left[0]:
            heapq.heappush(self.left, num)
        else:
            heapq.heappush(self.right, -1 * num)
        
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
               extra = -1 * heapq.heappop(self.left)
               heapq.heappush(self.right, extra)
            else:
                extra = -1 * heapq.heappop(self.right)
                heapq.heappush(self.left, extra)




        

    def findMedian(self) -> float:
        print(self.left, self.right)
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (self.left[0] + (-1 * self.right[0]))/2
        elif len(self.left) > len(self.right):
            return self.left[0]
        return self.right[0] * -1
        
        