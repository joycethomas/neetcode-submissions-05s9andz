class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROW or c >= COL or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                res = dfs(r + dr, c + dc)
            return 
        
        islands = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands

            