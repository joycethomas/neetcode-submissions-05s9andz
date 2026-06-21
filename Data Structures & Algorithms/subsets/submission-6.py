class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs, curr = [], []

        def helper(i):
            if i >= len(nums):
                subs.append(curr.copy())
                return
            
            curr.append(nums[i])
            helper(i + 1)
            curr.pop()
            helper(i + 1)

        helper(0)
        return subs
        