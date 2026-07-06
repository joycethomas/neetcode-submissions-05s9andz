"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        if root:
            q.append(root)
        
        #print(q[-1].val)
        while len(q) > 0:
            prev = q[-1]
            for i in range(len(q)):
                curr = q.popleft()
                if i > 0:
                    prev.next = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                prev = curr
            prev = None
        
        return root
