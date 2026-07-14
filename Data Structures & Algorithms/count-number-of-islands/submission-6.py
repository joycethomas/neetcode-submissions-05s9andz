class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        vis = set()
        res = 0
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            vis.add((r, c))
            while q:
                rows, cols = q.popleft()
                for dr, dc in dir:
                    ro, co = rows + dr, cols + dc
                    if min(ro, co) >= 0 and ro < ROW and co < COL and grid[ro][co] == "1" and (ro, co) not in vis:
                        q.append((ro, co))
                        vis.add((ro, co))

                
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and (i, j) not in vis:
                    bfs(i, j)
                    res += 1
        return res
        
            
        