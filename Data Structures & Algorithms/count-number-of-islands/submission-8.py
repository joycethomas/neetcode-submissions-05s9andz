class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROW or c >= COL or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
            return 
        
        islands = 0
        for ro in range(ROW):
            for co in range(COL):
                if grid[ro][co] == "1":
                    dfs(ro, co)
                    islands += 1
        return islands
        