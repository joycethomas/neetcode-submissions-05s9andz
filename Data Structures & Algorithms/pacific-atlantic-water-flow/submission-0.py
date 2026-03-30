class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])

        for r in range(rows):
            self.dfs(r, 0, pac, heights, heights[r][0])
            self.dfs(r, cols - 1, atl, heights, heights[r][cols - 1])
        for c in range(cols):
            self.dfs(0, c, pac, heights, heights[0][c])
            self.dfs(rows - 1, c, atl, heights, heights[rows - 1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res


    def dfs(self, r, c, visit, grid, prev):
        if((r, c) in visit 
        or r not in range(len(grid)) 
        or c not in range(len(grid[0])) 
        or grid[r][c] < prev):
            return

        visit.add((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            self.dfs(dr + r, dc + c, visit, grid, grid[r][c])



        