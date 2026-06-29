class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        vis = set()

        def dfs(r, c, ind):
            if ind == len(word):
                return True
            if min(r, c) < 0 or r == ROW or c == COL or (r, c) in vis or board[r][c] != word[ind]:
                return False
            
            ind += 1

            vis.add((r, c))
            res = dfs(r + 1, c, ind) or dfs(r - 1, c, ind) or dfs(r, c + 1, ind) or dfs(r, c - 1, ind)
            vis.remove((r, c))

            return res
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False

        