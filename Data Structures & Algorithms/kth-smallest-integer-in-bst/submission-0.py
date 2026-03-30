# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []
        curr = root

        while stack or curr:
            if curr: 
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                count += 1
                if count == k:
                    return curr.val
                curr = curr.right
        

        #make a list of tricks for trees
        '''- bfs
        - dfs
        - in order
        - post order
        - pre order
        - just look at the rest of the notes and figure it out '''
        