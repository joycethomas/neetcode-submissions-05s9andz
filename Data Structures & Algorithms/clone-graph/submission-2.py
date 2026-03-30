"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        old2New = {}

        def dfs(n):
            if n is None:
                return None
            if n in old2New:
                return old2New[n]
            copy = Node(n.val)
            old2New[n] = copy
            for x in n.neighbors:
                copy.neighbors.append(dfs(x))
            return copy

        dfs(node)
        return old2New[node]