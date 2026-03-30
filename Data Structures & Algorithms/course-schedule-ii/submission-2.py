class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''if not prerequisites:
            return []'''
        
        adj = {}
        '''for x, y in prerequisites:
            if x not in adj:
                adj[x] = []
            if y not in adj:
                adj[y] = []
            adj[x].append(y)'''
        for x in range(numCourses):
            adj[x] = []
        for x, y in prerequisites:
            adj[x].append(y)
        
        vis = set()
        path = []

        def dfs(n):
            if n in vis:
                return False
            if not adj[n]:
                if n not in path:
                    path.append(n)
                return True
            
            vis.add(n)
            for nei in adj[n]:
                if not dfs(nei): return False
            adj[n] = []
            if n not in path:
                path.append(n)
            vis.remove(n)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
            #path.append(crs)

        return path
        