class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        currmax = 1
        currmin = 1
        maxsum = max(nums)

        for n in nums:
            if n == 0:
                currmax = 1
                currmin = 1
                continue
            tmp = currmax * n #because we're abotu to change currmax
            currmax = max(currmax * n, currmin * n, n) #doing this because it could be like the new value is negative, so currmin (which is maybe negative) could then turn into currmax
            currmin = min(tmp, currmin * n, n)
            maxsum = max(maxsum, currmax)
    
        return maxsum


        