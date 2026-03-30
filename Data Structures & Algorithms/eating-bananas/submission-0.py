class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r
        while l <= r:
            mid = (l + r)//2
            #print(mid, l , r)
            hours = 0
            for x in piles:
                hours += math.ceil(x/mid)
            if hours <= h: 
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1

        return k
                

               