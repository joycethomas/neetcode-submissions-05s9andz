class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        vis = set()
        ROW, COL = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROW or c >= COL or (r, c) in vis or grid[r][c] == 1:
                return 0
            if r == ROW - 1 and c == COL - 1:
                return 1
            count = 0
            vis.add((r, c))
            for dr, dc in directions: 
                count += dfs(dr + r, dc + c)
            vis.remove((r, c))
            return count
        
        return dfs(0, 0)
                