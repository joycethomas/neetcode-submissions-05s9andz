"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]
            copy = Node(node.val)
            clones[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        if node:
            return dfs(node)
        else:
            return None













        '''clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]
            
            copy = Node(node.val)
            clones[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
            
        if node:
            return dfs(node)
        else:
            return None'''


        '''clonetracker = {}
        
        def dfs(node):
            if node in clonetracker:
                return clonetracker[node]

            copy = Node(node.val)
            clonetracker[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        if node:
            return dfs(node)
        else:
            return None'''
        