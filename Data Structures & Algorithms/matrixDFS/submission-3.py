class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        self.ROW = len(grid)
        self.COL = len(grid[0])
        visited = set()

        def dfs(r, c, visited):
            print(r, c)
            if min(r, c) < 0 or r >= self.ROW or c >= self.COL or (r, c) in visited or grid[r][c] == 1:
                return 0
            if r == self.ROW - 1 and c == self.COL - 1:
                return 1
            
            count = 0
            visited.add((r, c))
            count += dfs(r + 1, c, visited)
            count += dfs(r - 1, c, visited)
            count += dfs(r, c + 1, visited)
            count += dfs(r, c - 1, visited)
            visited.remove((r, c))

            return count
        return dfs(0, 0, visited)
        
        