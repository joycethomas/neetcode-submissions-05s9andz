class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combo, curr = [],[]

        def helper(i, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                combo.append(curr.copy())
                return
            
            
            curr.append(nums[i])
            total += nums[i]
            helper(i, total)

            curr.pop()
            total -= nums[i]
            helper(i + 1, total)
        
        helper(0, 0)
        return combo