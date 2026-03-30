class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        atvis = set()
        atres = []
        atq = collections.deque()
        pacvis = set()
        pacres = []
        pacq = collections.deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(ROW):
            atq.append((r, 0))
            atvis.add((r, 0))
            atres.append((r, 0))
            pacq.append((r, COL - 1))
            pacvis.add((r, COL - 1))
            pacres.append((r, COL - 1))
        for c in range(COL):
            atq.append((0, c))
            atvis.add((0, c))
            atres.append((0, c))
            pacq.append((ROW - 1, c))
            pacvis.add((ROW - 1, c))
            pacres.append((ROW - 1, c))
        

        def bfs(q, vis, res):
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    '''if (r, c) in vis:
                        return'''
                    for dr, dc in directions:
                        if (r + dr, c + dc) in vis or min(dr + r, dc + c) < 0 or r + dr >= ROW or c + dc >= COL: 
                            continue
                        if heights[r + dr][c + dc] >= heights[r][c]:
                            q.append((r + dr, c + dc))
                            res.append((r + dr, c + dc))
                            vis.add((r + dr, c + dc))

        bfs(atq, atvis, atres)
        bfs(pacq, pacvis, pacres)

    
        print(atres, pacres)
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in atres and (r, c) in pacres:
                    res.append([r, c])

        return res
