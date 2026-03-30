class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = [],[]
        pvis, avis = set(), set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c, res, vis, prevHeight):
            if min(r, c) < 0 or r >= ROW or c >= COL or (r, c) in vis or heights[r][c] < prevHeight:
                return
            if heights[r][c] >= prevHeight:
                res.append((r, c))
                vis.add((r, c))
            for dr, dc in directions:
                dfs(dr + r, dc + c, res, vis, heights[r][c])
                #vis.add((dr + r, dc + c))

        for r in range(ROW):
            dfs(r, 0, pac, pvis, heights[r][0])
            dfs(r, COL - 1, atl, avis, heights[r][COL - 1])

        for c in range(COL):
            dfs(0, c, pac, pvis, heights[0][c])
            dfs(ROW - 1, c, atl, avis, heights[ROW - 1][c])
        
        print(atl, pac)
        result = []
        for x in pac:
            if x in atl:
                r, c = x
                result.append([r, c])
        return result

