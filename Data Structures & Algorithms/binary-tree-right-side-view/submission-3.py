# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []
        result = []
        queue = deque()
        queue.append(root)
        curr = root.val
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(curr.val)

        '''self.result = []

        def dfs(root):
            if root is None: 
                return
            self.result.append(root.val)
            dfs(root.right)
        
        dfs(root)'''
        return result


        