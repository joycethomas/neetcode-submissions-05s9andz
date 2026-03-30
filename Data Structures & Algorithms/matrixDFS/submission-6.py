class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        vis = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROW, COL = len(grid), len(grid[0])
        #length = 0

        def dfs(r, c):
            #print(r, c)
            if min(r, c) < 0 or r >= ROW or c >= COL or (r, c) in vis or grid[r][c] == 1:
                return 0
            if r == ROW - 1 and c == COL - 1:
                return 1
            vis.add((r, c))
            count = 0
            for dr, dc in directions:
                count += dfs(dr + r, dc + c)
            vis.remove((r, c))
            return count
        
        return dfs(0, 0)
