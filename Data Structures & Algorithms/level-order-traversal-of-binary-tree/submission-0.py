# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()

        queue.append(root)
        result = []

        j = 0
        while queue:
            result.append([])
            for i in range(len(queue)):
                #get curr
                curr = queue.popleft()
                result[j].append(curr.val)
                #add the children
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            j += 1

        return result


        