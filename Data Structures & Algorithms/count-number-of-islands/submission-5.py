class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        vis = set()
        res = 0

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROW or c >= COL or (r, c) in vis or grid[r][c] == "0":
                return
            
            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            grid[r][c] = "0"
            for dr, dc in dir:
                dfs(r + dr, c + dc)
            

            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in vis:
                    dfs(r, c)
                    res += 1
        return res
        