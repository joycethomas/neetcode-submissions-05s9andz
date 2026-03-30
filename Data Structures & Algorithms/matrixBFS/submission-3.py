class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        def bfs(grid):
            ROW = len(grid)
            COL = len(grid[0])

            q = collections.deque()
            visited = set()
            q.append((0, 0))
            visited.add((0, 0))

            length = 0

            while q: 
                for i in range(len(q)):
                    r, c = q.popleft()
                    if r == ROW - 1 and c == COL - 1:
                        return length

                    neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in neighbors:
                        if min(r + dr, c + dc) < 0 or r + dr >= ROW or c + dc >= COL or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visited:
                            continue
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
                length += 1

            return -1
        
        return bfs(grid)



        