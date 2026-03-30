# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #keep track of lowest on each level and highest on each level
        if root is None: 
            return True
        def dfs(root, low, high):
            if root is None: 
                return True
            if root.val > low and root.val < high:
                return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
            return False
        
        return dfs(root.left, -1001, root.val) and dfs(root.right, root.val, 1001)