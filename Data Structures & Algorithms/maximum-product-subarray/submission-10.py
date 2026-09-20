class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        posmax = 1
        negmax = 1
        res = float('-inf')

        for n in nums:
            if n == 0:
                posmax = 1
                negmax = 1
            tmp = posmax
            posmax = max(posmax * n, negmax * n, n)
            negmax = min(tmp * n, negmax * n, n)
            res = max(posmax, res)
        return res
