class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        
        heapq.heapify(nums)
        res = 0
        counter = 0
        while counter < k:
            res = heapq.heappop(nums)
            counter += 1
        
        return res * -1
        