class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combo = []

        def helper(i, comb, curr, k, n):
            if len(curr) == k:
                comb.append(curr.copy())
                return
            if i > n:
                return
            
            for j in range(i, n + 1):
                curr.append(j)
                helper(j + 1, combo, curr, k, n)
                curr.pop()
            
        helper(1, combo, [], k, n)
        return combo
        