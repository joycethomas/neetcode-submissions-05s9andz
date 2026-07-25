class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        n = len(nums)
        dp = [0] * n
        dp[-1], dp[-2] = nums[-1], nums[-2]
        maxProf = 0

        i = len(nums) - 3
        while i >= 0:
            maxProf = max(maxProf, dp[i + 2])
            dp[i] = nums[i] + maxProf
            i -= 1
            print(nums[i], maxProf, dp)
        
        return max(dp[0], dp[1])


        