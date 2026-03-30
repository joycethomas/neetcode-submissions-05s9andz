class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visit = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visit:
                    self.dfs(r, c, visit, grid)
                    islands += 1
        return islands
    
    def dfs(self, r, c, visit, grid):
        if(r not in range(len(grid))
            or c not in range(len(grid[0]))
            or (r, c) in visit 
            or grid[r][c] == "0"):
                return 
        visit.add((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for dr, dc in directions:
            self.dfs(r + dr, c + dc, visit, grid)

            
        



















'''
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])


        def dfs(r, c):
            if(r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit):
                return
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions: 
                dfs(r + dr, c + dc)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands


    #bfs iteratively
    def bfs(r, c):
        q = collections.deque()
        visit.add(r, c)
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if(r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))'''
         



#lmao practicing the dfs
'''def dfs(r, c, visit, grid): #visit is a set
    if(r not in range(len(grid)) or c not in range(len(grid[0])) or (r, c) in visit or grid[r][c] == "0"):
        return 
    visit.add((r, c))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dr, dc in directions:
        dfs(r + dr, c + dc, visit, grid)


def dfs(r, c, grid, visit):
    if(r not in range(len(grid)) or c not in range(len(grid[0])) or (c, r) in visit or grid[r][c] == "0"):
        return
    visit.add((r, c))
    directions = [[1, 0], [-1, 0], [0, 1],[0, -1]]
    for dr, dc in directions:
        dfs(r + dr, c + dc, grid, visit)


def dfs(r, c, visit): #visit is going to be a set
    if(r not in range(rows) or c not in range(cols) or (r, c) in visit or grid[r][c] == "0"):
        return 
    visit.add((r, c))
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dr, dc in directions: 
        bfs(r + dr, c + dc)'''







