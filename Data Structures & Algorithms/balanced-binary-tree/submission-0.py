# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return True
        self.flag = True
        #the problem is that i'm not updating how many leaves there are 
        def bfs(curr):
            if curr is None: 
                return 0

            right = bfs(curr.right)
            left = bfs(curr.left)
            if abs(left - right) > 1: 
                self.flag = False
            return max(1 + bfs(curr.right), 1 + bfs(curr.left))
        
        bfs(root)
        return self.flag
        
            
    