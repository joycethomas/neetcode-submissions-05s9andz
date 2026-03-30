"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old2New = {}

        def dfs(n):
            if n in old2New:
                return old2New[n]
            copy = Node(n.val)
            old2New[n] = copy
            for x in n.neighbors:
                if x not in old2New:
                    dfs(x)
                copy.neighbors.append(old2New[x])

        dfs(node)
        return old2New[node]

            

        