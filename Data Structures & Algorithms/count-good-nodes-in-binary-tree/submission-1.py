# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.result = 0
        maxval = root.val

        def dfs(root, maxval): #should return a 1 if it increases the result
            if root is None:
                return
            if root.val >= maxval:
                self.result += 1
                maxval = root.val
            dfs(root.right, maxval)
            dfs(root.left,maxval)
        
        dfs(root, maxval)
        return self.result
            

        
        