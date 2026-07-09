# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node
            
            side1 = dfs(node.right)
            side2 = dfs(node.left)

            if side1 and side2:
                return node
            if side1:
                return side1
            if side2:
                return side2
            return None

        return dfs(root)
        