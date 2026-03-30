# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = float('-inf')
        high = float('inf')
        return self.dfs(root, low, high)

    def dfs(self, root, low, high):
        if root is None:
            return True
        if root.val <= low or root.val >= high:
            return False
        '''if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val):
            return False
        if (root.left and not root.right and root.left.val < root.val) or (root.right and not root.left and root.right.val < root.val):
            return True'''
        return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, high)

        