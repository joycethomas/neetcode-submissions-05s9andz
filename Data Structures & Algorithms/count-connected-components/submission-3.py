class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = set()
        path = set()
        adj = {}
        
        for x in range(n):
            adj[x] = []
        
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(node):
            if node in vis:
                return False
            '''if node in path:
                return True'''
            '''if adj[node] == []:
                path.add(node)
                #return True'''
            '''if adj[node] == [prev]:
                return True'''
            
            vis.add(node)
            path.add(node)
            #print(node, adj[node])
            for nei in adj[node]:
                if not dfs(nei): continue
            adj[node] = []
            vis.remove(node)
            return True
        
        result = 0
        for x in range(n):
            if x not in path:
                result += 1
                dfs(x)
            #print("new run")
            #print(x, path)
        print(result)
        return result

            
        