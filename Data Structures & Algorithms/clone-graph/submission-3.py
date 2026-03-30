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
        q = collections.deque()
        q.append(node)
        old2New[node] = Node(node.val)
        
        while q:
            curr = q.popleft()
            #old2New[curr] = Node(curr.val)
            for x in curr.neighbors:
                if x not in old2New:
                    q.append(x)
                    old2New[x] = Node(x.val)
                old2New[curr].neighbors.append(old2New[x])

        return old2New[node]
