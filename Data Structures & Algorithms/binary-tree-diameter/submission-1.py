# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        #function to return the height - does two things: potentially update the result and return the height of the tree from curr
        def dfs(curr):
            if curr is None: 
                return 0
            right = dfs(curr.right)
            left = dfs(curr.left)
            self.d = max(self.d, right + left)
            return max(1 + dfs(curr.left), 1 + dfs(curr.right))

        dfs(root)
        return self.d

        