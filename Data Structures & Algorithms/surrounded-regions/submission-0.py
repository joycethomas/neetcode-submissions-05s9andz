class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        vis = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ohs = set()

        def dfs(r, c):
            #base case
            if min(r, c) < 0 or r >= ROW or c >= COL or (r, c) in vis or board[r][c] == 'X':
                return
            ohs.add((r, c))
            vis.add((r, c))
            for dr, dc in directions:
                row, col = r + dr, c + dc
                res = dfs(row, col)
            vis.remove((r, c))
        
        
        for r in range(ROW): 
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COL - 1] == 'O':
                dfs(r, COL - 1)
        for c in range(COL):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROW - 1][c] == 'O':
                dfs(ROW - 1, c)

        for r in range(ROW):
            for c in range(COL):
                if (r, c) in ohs:
                    continue
                board[r][c] = 'X'

        