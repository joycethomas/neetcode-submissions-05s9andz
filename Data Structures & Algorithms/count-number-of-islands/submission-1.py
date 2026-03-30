class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visit = set()
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visit:
                    self.dfs(row, col, visit, grid)
                    count += 1
        return count
                    
    def dfs(self, r, c, visit, grid):
        if ((r, c) in visit
            or r not in range(len(grid))
            or c not in range(len(grid[0]))
            or grid[r][c] == "0"):
            return 
        visit.add((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in directions:
            self.dfs(dr + r, dc + c, visit, grid)

    















    '''def bfs(r, c, visit, grid): #iterative
        q = collections.deque()
        visit.add((r, c))
        q.append((r, c))
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = dr + r, dc + c
                if(r in range(len(grid)) and
                c in range(len(grid[0])) and
                (r, c) not in visit and
                grid[r][c] == "1"):
                q.append((r, c))
                visit.add((r, c))'''
