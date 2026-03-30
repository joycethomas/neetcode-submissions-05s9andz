class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        result = -1


        def bfs(grid):
            self.ROW = len(grid)
            self.COL = len(grid[0])
            q = collections.deque()
            visited = set()
            q.append((0, 0))
            visited.add((0, 0))
            length = 0

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    #r, c = curr[0], curr[1]
                    if r == self.ROW - 1 and c == self.COL - 1:
                        #return 1
                        return length

                    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in directions: 
                        if min(r + dr, c + dc) < 0 or r + dr >= self.ROW or c + dc >= self.COL or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visited:
                            continue
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
                length += 1

            #return length
            return -1
        
        return bfs(grid)

