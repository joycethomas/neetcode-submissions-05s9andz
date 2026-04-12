class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combo = []

        def helper(i, curr, comb, k, n):
            if len(curr) == k:
                comb.append(curr.copy())
                return
            if i > n:
                return
            
            for j in range(i, n + 1):
                curr.append(j)
                helper(j + 1, curr, comb, k, n)
                curr.pop()

            
        helper(1, [], combo, k, n)
        return combo
        