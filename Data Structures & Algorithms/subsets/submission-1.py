class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs, currsub = [], []

        def helper(i, sub, curr, nums):
            if i >= len(nums):
                sub.append(curr.copy())
                return
            
            curr.append(nums[i])
            helper(i + 1, sub, curr, nums)
            curr.pop()
            
            helper(i + 1, sub, curr, nums)
        
        helper(0, subs, currsub, nums)
        return subs
