class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()
        visited = set()

        q.append((0, 0))
        visited.add((0, 0))
        result = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return result
                for dr, dc in directions:
                    if min(r + dr, c + dc) < 0 or r + dr >= ROW or c + dc >= COL or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visited:
                        continue
                    q.append((r + dr, c + dc))
                visited.add((r, c))
            result += 1
        
        return -1
        
