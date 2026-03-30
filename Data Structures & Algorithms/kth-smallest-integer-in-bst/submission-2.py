# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #keep a list of k smallest integers
        #if the list grows past k, cut off the biggest number
        #keep going left unti you can, othewise go right
        #sounds like we'll need dfs
        self.q = collections.deque()

        #keep recursing left
        #if it hits a None, and then we need more values, then go the right
        def dfs(root, k):
            if not root: return
            if root.left: 
                dfs(root.left, k)
            self.q.append(root.val)
            print(self.q)
            if len(self.q) == k:
                return
            dfs(root.right, k)
            #self.q.append(root.val)
            '''if len(self.q) == k:
                return'''
            return
            


        dfs(root, k)
        #print(len(self.q))
        return self.q[k - 1]
            


        