class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def robber(subnums):
            if not subnums:
                return 0
            if len(subnums) == 1:
                return subnums[0]
            if len(subnums) == 2:
                return max(subnums[0], subnums[1])
            n = len(subnums)
            dp = [0] * n
            dp[-1], dp[-2] = subnums[-1], subnums[-2]
            maxProf = 0

            i = len(subnums) - 3
            while i >= 0:
                maxProf = max(maxProf, dp[i + 2])
                dp[i] = subnums[i] + maxProf
                i -= 1
                print(nums[i], maxProf, dp)
            
            return max(dp[0], dp[1])
        
        return max(robber(nums[1:]), robber(nums[:-1]))
