# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        
        rights = self.invertTree(root.right)
        lefts = self.invertTree(root.left)

        temp = lefts
        root.left = rights
        root.right = lefts

        return root


        