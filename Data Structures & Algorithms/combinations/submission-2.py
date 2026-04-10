class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combos = []

        def helper(i, curr, combo, k):
            if len(curr) == k:
                combo.append(curr.copy())
                return
            if i > n:
                return

            for j in range(i, n + 1):
                curr.append(j)
                helper(j + 1, curr, combo, k)
                curr.pop()

        helper(1, [], combos, k)            
        return combos
            