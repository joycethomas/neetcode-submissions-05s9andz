class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #wouldn't use bfs for this because we're not trying to find the shortest path
        #let's go with dfs
        if not grid: 
            return 0
        ROW = len(grid)
        COL = len(grid[0])
        results = 0

        '''r, c = 0, 0
        neighbors = [[1, 0],[-1, 0], [0, 1], [0, -1]]
        if 
        for dr, dc in neighbors:
            if 
        if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] == 0:
            return 0'''

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROW or c >= COL or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            directions = [[0, 1],[0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
    
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r, c)
                    results += 1
        return results



        