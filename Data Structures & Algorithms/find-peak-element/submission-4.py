class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return 0
        if nums[l] > nums[l + 1]:
            return l
        if nums[r] > nums[r - 1]:
            return r

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            if nums[m + 1] > nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        