class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combo = []

        def helper(i, curr, total):
            if total == target:
                combo.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            total += nums[i]
            curr.append(nums[i])
            helper(i, curr, total)

            curr.pop()
            total -= nums[i]
            helper (i + 1, curr, total)
        
            
            '''for j in range(i, len(n)):
                curr.append(n[j])
                total += n[j]
                helper(j + 1, comb, curr, target, total, n)
                curr.pop
                total -= n[j]'''
            
        helper(0, [], 0)
        return combo
