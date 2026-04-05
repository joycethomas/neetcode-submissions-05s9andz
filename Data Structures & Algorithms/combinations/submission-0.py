class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combs = []

        def helper(i, curcomb, n, k):
            if len(curcomb) == k:
                self.combs.append(curcomb.copy())
                return 
            if i > n:
                return 
            
            for j in range(i, n + 1):
                curcomb.append(j)
                helper(j + 1, curcomb, n, k)
                curcomb.pop()
        
        helper(1, [], n, k)
        return self.combs
        