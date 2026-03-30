"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# i think i have the general concept, i just don't understand how classes work lmao
# time to check the solution
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        old2New = {}
        
        def dfs(n):
            if not node: 
                return None
            if n in old2New:
                return old2New[n]
            copy = Node(n.val)
            #old2New[n] = Node(n.val)
            old2New[n] = copy
            for x in n.neighbors: 
                #nei = dfs(x)
                #if nei:
                    #old2New.get(x).neighbors.append(nei)
                copy.neighbors.append(dfs(x))
            return old2New[n]
        
        dfs(node)
        return old2New[node]


