class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, pos, neg = set(), set(), set()
        res = []
        grid = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in grid]
                res.append(copy)
                return


            for c in range(n):
                if c in col or (r + c) in pos or (r - c) in neg:
                    continue
                pos.add(r + c)
                neg.add(r - c)
                col.add(c)
                grid[r][c] = "Q"

                dfs(r + 1)

                pos.remove(r + c)
                neg.remove(r - c)
                col.remove(c)
                grid[r][c] = "."


        dfs(0)
        
        return res

        