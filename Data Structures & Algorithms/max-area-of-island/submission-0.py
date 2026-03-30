class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = 0

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROW or c >= COL or grid[r][c] == 0:
                return 0
            '''if grid[r][c] == 1:
                return 1'''
            count = 0
            grid[r][c] = 0
            count += 1
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            return count

        for r in range(ROW):
            for c in range(COL):
                result = max(result, dfs(r, c))
        
        return result
        