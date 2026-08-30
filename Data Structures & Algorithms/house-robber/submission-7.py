class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * (len(nums))
        dp[-1], dp[-2] = nums[-1], max(nums[-1], nums[-2])
        print(dp)
        i = len(nums) - 3


        while i >= 0:
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
            i -= 1


        return dp[0]