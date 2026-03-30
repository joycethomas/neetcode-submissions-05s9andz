class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None

        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        q = collections.deque()
        '''visited.add((0, 0))
        q.append((0, 0))'''
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        level = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = min(grid[r][c], level)
                for dr, dc in directions:
                    if min(r + dr, c + dc) < 0 or dc + c >= COL or dr + r >= ROW or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == -1:
                        continue
                    q.append((r + dr, c + dc))
                visited.add((r, c))
            level += 1