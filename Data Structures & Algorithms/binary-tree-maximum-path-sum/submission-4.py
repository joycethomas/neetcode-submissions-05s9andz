# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.prev = root.val

        def dfs(root):
            '''if root and not root.left and not root.right:
                return root.val'''
            if not root: 
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            #the problem is how do i consider if the parent sum is 
            #better than including the current node
            self.prev = max(self.prev, root.val + left + right)
    
            return max(left + root.val, right + root.val, root.val)


        dfs(root)
        return self.prev
            