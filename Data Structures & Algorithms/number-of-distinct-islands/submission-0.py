class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = set()

        def dfs(r, c, r0, c0, normal):
            if min(r, c) < 0 or r >= ROW or c >= COL or grid[r][c] == 0:
                return 
            
            grid[r][c] = 0
            normal.append((r - r0, c - c0))

            for dr, dc in dir:
                dfs(r + dr, c + dc, r0, c0, normal)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    frozen = []
                    dfs(r, c, r, c, frozen)
                    frozen.sort()
                    islands.add(tuple(frozen))

        return len(islands)


        