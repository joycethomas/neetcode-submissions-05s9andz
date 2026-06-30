class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subs, curr = [], []
        nums.sort()

        def helper(i):
            if i >= len(nums):
                subs.append(curr.copy())
                return 
            
            curr.append(nums[i])
            helper(i + 1)
            curr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1)
        
        helper(0)
        return subs

        