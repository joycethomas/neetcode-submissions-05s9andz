class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []

        def helper(i, curr, combo, nums, currsum, target):
            if i >= len(nums) or currsum > target: 
                return 
            
            if currsum == target:
                combos.append(curr.copy())
                return
            
            
            curr.append(nums[i])
            currsum += nums[i]
            helper(i, curr, combo, nums, currsum, target)
            currsum -= nums[i]
            curr.pop()

            helper(i + 1, curr, combo, nums, currsum, target)

        

        helper(0, [], combos, nums, 0, target)
        return combos
        