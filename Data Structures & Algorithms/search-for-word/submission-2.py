class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #count =len(word)
        vis = set()
        ROW = len(board)
        COL = len(board[0])

        def dfs(r, c, vis, ind):
            if ind == len(word):
                return True
            print(ind)
            if r < 0 or c < 0 or r == ROW or c == COL or (r, c) in vis or board[r][c] != word[ind]:
                return False
            ind += 1
                
            
            #need to figure out a way to increment length if it is following the order
            #maybe have like a before variable and see if it goes in order

            vis.add((r, c))
            '''if dfs(r + 1, c, vis, ind):
                return True
            if dfs(r, c + 1, vis, ind):
                return True
            if dfs(r - 1, c, vis, ind):
                return True
            if dfs(r, c - 1, vis, ind):
                return True'''
            if dfs(r + 1, c, vis, ind) or dfs(r, c + 1, vis, ind) or dfs(r - 1, c, vis, ind) or dfs(r, c - 1, vis, ind):
                return True
                
            vis.remove((r, c))

            return False

        for r in range(ROW): 
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r, c, vis, 0):
                        return True
        return False
        