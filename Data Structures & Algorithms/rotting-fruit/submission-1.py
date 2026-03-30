class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None: 
            return None
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        level = 0
        flag = False
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                #grid[r][c] = 2
                for dr, dc in directions:
                    if min(dr + r, dc + c) < 0 or dr + r >= ROW or c + dc >= COL or (dr + r, dc + c) in visited or grid[dr + r][dc + c] == 2 or grid[dr + r][dc + c] == 0:
                        continue
                    flag = True
                    q.append((dr + r, dc + c))
                    visited.add((dr + r, dc + c))
                    grid[r + dr][c + dc] = 2
            if flag:
                level += 1
                flag = False

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return -1
        return level