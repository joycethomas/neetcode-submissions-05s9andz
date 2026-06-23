class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combo, curr = [], []
        candidates.sort()

        def helper(i, total):
            if total == target: 
                combo.append(curr.copy())
                return
            if i > len(candidates) or total > target:
                return

            for j in range(i, len(candidates)):
                if candidates[j - 1] == candidates[j] and j > i:
                    continue
                curr.append(candidates[j])
                helper(j + 1, total + candidates[j])
                curr.pop()
                #helper(j + 1, total)
            
        helper(0, 0)
        return combo

        