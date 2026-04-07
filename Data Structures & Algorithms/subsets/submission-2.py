class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs, curr = [],[]
        
        
        def helper(i, subset, currsub, nums):
            if i >= len(nums):
                subset.append(currsub.copy())
                return 

            currsub.append(nums[i])
            helper(i + 1, subset, currsub, nums)
            currsub.pop()

            helper(i + 1, subset, currsub, nums)

        
        helper(0, subs, curr, nums)
        return subs