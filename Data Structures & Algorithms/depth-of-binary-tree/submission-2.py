# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        
        lsum = 1 + self.maxDepth(root.left)
        rsum = 1 + self.maxDepth(root.right)
        
        return max(lsum, rsum)
        