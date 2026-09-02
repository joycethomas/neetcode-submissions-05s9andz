class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def robber(nums):
            dp1, dp2 = 0, 0

            for n in nums:
                temp = max(dp2, dp1 + n)
                dp1, dp2 = dp2, temp
            
            return dp2

        rob1 = robber(nums[1:])
        rob2 = robber(nums[:-1])
        print(rob1, rob2)
        return max(rob1, rob2)