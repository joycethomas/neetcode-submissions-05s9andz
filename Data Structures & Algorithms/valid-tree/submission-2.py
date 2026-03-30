class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and len(edges) == 1:
            return False
        adj = {}
        for x in range(n):
            adj[x] = []
        
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()
        cycle = set()
        def dfs(n):
            print(n)
            if n in cycle:
                return False
            if not adj[n] or n in visited:
                return True
            
            visited.add(n)
            for nei in adj[n]:
                if not dfs(nei): return False
            visited.remove(n)
            cycle.add(n)
            return True
        
        if not dfs(0): return False

        for node in range(1, n):
            if node not in cycle: 
                print("node", node, cycle)
                return False
        return True

        

        


        