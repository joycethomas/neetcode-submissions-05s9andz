class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        q = collections.deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        level = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = level

                for dr, dc in directions:
                    if min(dr + r, c + dc) < 0 or dr + r >= ROW or c + dc >= COL or grid[r + dr][dc + c] == -1 or (dr + r, dc + c) in visited:
                        continue
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            level += 1
