# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None: 
            return True
        if root is None and subRoot: 
            return False

        def sameTree(p, q):
            if p is None and q is None:
                return True
            if p is None and q or p and q is None:
                return False
            if p.val != q.val:
                return False
            if p.val == q.val: 
                return sameTree(p.right, q.right) and sameTree(p.left, q.left)
        
        if root.val == subRoot.val:
            flag = sameTree(root, subRoot)
            if flag:
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)