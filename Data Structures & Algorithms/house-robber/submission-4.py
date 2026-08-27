class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp1, dp2 = nums[-1], max(nums[-1], nums[-2])
        biggest = 0
        i = len(nums) - 3

        while i >= 0:
            current = max(nums[i] + dp1, dp2)
            dp1, dp2 = dp2, current
            i -=1

        return dp2