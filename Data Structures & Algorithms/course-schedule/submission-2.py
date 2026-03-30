class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj = {}
        for x, y in prerequisites:
            if x not in adj:
                adj[x] = []
            if y not in adj:
                adj[y] = []
            adj[x].append(y)
        
        visited = set()
        #path = set()
        def dfs(n):
            if n in visited:
                return False
            if not adj[n]:
                #path.add(n)
                return True
            
            visited.add(n)
            for nei in adj[n]:
                if not dfs(nei): return False
            visited.remove(n)
            adj[n] = []
            return True            
        

        for crs in adj:
            if not dfs(crs): return False
        return True